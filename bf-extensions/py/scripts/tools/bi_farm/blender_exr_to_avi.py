# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

# this script _must_ run from inside blender.

import bpy
import sys
import os

# weak
sys.path.append("/shared/software/render_farm/")

def exr_size(filepath):
    # check for 'dataWindow (type box2i): (0 0) - (4095 2159)'
    # in the command 'exrheader' output
    # get the size of the first image.
    # We need to add 1 for some reason... its how EXR works.
    import subprocess
    process = subprocess.Popen(["exrheader", filepath],
                               stdout=subprocess.PIPE,
                               )
    process.wait()
    out = process.stdout.read()
    process.stdout.close()

    for l in out.split(b"\n"):
        if l.startswith(b"dataWindow "):
            l = l.decode("ascii").rsplit("(", 1)[-1].strip(")").strip()
            width, height = [int(w) + 1 for w in l.split()]
            return width, height

    raise Exception("can't find dataWindow size")


def main():

    # -------------------------------------------------------------------------
    # Find frames to convert
    import new_blend_2_frames

    image_dir = sys.argv[-2]
    blendfile = sys.argv[-1]

    if not image_dir.endswith("/"):
        image_dir += "/"

    frames = new_blend_2_frames.blend_2_frames(blendfile)
    # print(frames, blendfile)

    # -------------------------------------------------------------------------
    # Setup the Scene
    scene = bpy.context.scene
    scene.sequence_editor_clear()
    scene.sequence_editor_create()

    # frames == [(f_nr, f_name), (f_nr, f_name), ...]
    seq = scene.sequence_editor.sequences.new_image(name="Image",
                                                    filepath=frames[0][1],
                                                    channel=1,
                                                    start_frame=1)
    for f_nr, f_name in frames[1:]:
        seq.elements.push(os.path.basename(f_name))

    scene.frame_start = 1
    scene.frame_end = len(frames)
    scene.render.use_sequencer = True
    scene.render.resolution_percentage = 50  # always render half the resolution
    if 0:  # hard coded?
        scene.render.resolution_x, scene.render.resolution_y = 1920, 800
    else:  # detect resolution of the EXR 
        scene.render.resolution_x, scene.render.resolution_y = exr_size(frames[0][1])

    scene.render.image_settings.file_format = 'AVI_JPEG'
    scene.render.image_settings.quality = 95
    scene.render.filepath = os.path.join(image_dir, os.path.basename(image_dir[:-1])) + ".avi"

    # -------------------------------------------------------------------------
    # Render the Scene
    bpy.ops.render.render(animation=True)


if __name__ == "__main__":
    main()