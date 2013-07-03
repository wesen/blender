#!/shared/software/python/bin/python3.2

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

# <pep8-80 compliant>

# used by slideshow generator

import bpy
import sys
import os.path

exr_name = sys.argv[-3]
png_name = sys.argv[-2]
percentage = int(sys.argv[-1])

dir, fname = os.path.split(exr_name)

files = [{"name": fname}]

bpy.ops.sequencer.image_strip_add(
        directory=dir,
        filter_blender=False,
        filter_image=True,
        filter_movie=False,
        frame_start=1,
        channel=1,
        replace_sel=True,
        files=files,
        )

# render
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 1
bpy.context.scene.render.use_sequencer = True
bpy.context.scene.render.resolution_percentage = percentage
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 800
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = png_name

# stamp original name
bpy.context.scene.render.use_stamp = True
bpy.context.scene.render.use_stamp_note = True
bpy.context.scene.render.stamp_note_text = os.path.splitext(fname)[0]
bpy.context.scene.render.stamp_font_size = 16

# disable all others
bpy.context.scene.render.use_stamp_time = False
bpy.context.scene.render.use_stamp_date = False
bpy.context.scene.render.use_stamp_render_time = False
bpy.context.scene.render.use_stamp_frame = False
bpy.context.scene.render.use_stamp_scene = False
bpy.context.scene.render.use_stamp_camera = False
bpy.context.scene.render.use_stamp_lens = False
bpy.context.scene.render.use_stamp_filename = False
bpy.context.scene.render.use_stamp_marker = False
bpy.context.scene.render.use_stamp_sequencer_strip = False

bpy.ops.render.render(animation=True)
