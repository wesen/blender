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

# runs on the nodes inside blender

import bpy
import os
import sys
import math
import base64

# FIXME - pass as an arg?
#from render_dirs import REND_DIR
REND_DIR = "/render/mango/frames"


#try:
#    import finals_config
#except:
#    print("finals_config not found")
#    sys.exit(1)


# TODO: cleanup this and use some nice arg parsing!
processor = sys.argv[-5]
output_fpath = sys.argv[-4]
render_frame = int(sys.argv[-3])
quality = sys.argv[-2] + " " + sys.argv[-1]

def get_ip():

    import socket
    import fcntl
    import struct

    def get_ip_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('ascii'))
        )[20:24])

    for iface in "eth0", "eth1", "eth2", "eth3", "eth0_rename":
        try:
            ip = get_ip_address(iface)
            break
        except:
            ip = socket.gethostname()

    return ip


def get_revision(filepath):
    '''returns the revision of this blendfile'''
    import subprocess
    lines = subprocess.Popen(["svn", "info", bpy.data.filepath],
                              stdout=subprocess.PIPE
                              ).communicate()[0].splitlines()
    rev = b""
    for l in lines:
        if l.startswith(b'Revision: '):
            rev = l.split()[-1]

    if rev:
        return int(rev)
    else:
        return -1


def local_register():
    """Blender wont auto-import scripts yet so we need to force it"""
    for text in bpy.data.texts:
        if text.use_module:
            name = text.name
            if name.endswith(".py"):
                try:
                    __import__(name[:-3])
                except:
                    import traceback
                    traceback.print_exc()


def check_footage():
    """Check if all the footage is here"""

    ok = True

    for clip in bpy.data.movieclips:
        abspath = bpy.path.abspath(clip.filepath, clip.library)
        if not os.path.exists(abspath):
            print("Clip {} is not found" . format(abspath))
            ok = False

    return ok


def main():
    ip = get_ip()
    fpath = bpy.data.filepath
    fname = os.path.splitext(os.path.basename(fpath))[0]
    output_fname = os.path.splitext(os.path.basename(output_fpath))[0]
    scene_current = bpy.context.scene
    tmpdir = "/tmp/mango_farm" + str(render_frame)

    print("loaded:", fpath, scene_current)

    # not working
    os.system("rm -rf %s" % tmpdir)
    os.system("mkdir %s" % tmpdir)
    bpy.context.user_preferences.filepaths.temporary_directory = tmpdir

    #bpy.context.user_preferences.system.image_tile_memory_limit = 256
    print("Setting up all scenes")
    for scene in bpy.data.scenes:
        rd = scene.render

        # file output
        rd.image_settings.file_format = 'OPEN_EXR'
        rd.image_settings.color_depth = '16'
        rd.image_settings.use_preview = True
        rd.filepath = os.path.join(REND_DIR, output_fname, "%s_######" % fname)
        rd.use_file_extension = True
        rd.use_placeholder = False
        rd.use_overwrite = False
        rd.use_free_unused_nodes = True

        rd.use_stamp_note = True
        rd.use_stamp_render_time = True
        rd.stamp_note_text = ("rev:%s, art_rev:%s, %s" %
                              (bpy.app.build_revision,
                               str(get_revision(fpath)),
                               ip))

        # stamp
        if quality != "File settings":
            rd.use_stamp = False
            rd.stamp_font_size = 18
            rd.stamp_foreground = 1.0, 1.0, 1.0, 1.0
            rd.stamp_background = 0.0, 0.0, 0.0, 0.75

        # performance/memory
        rd.use_free_image_textures = True
        rd.use_save_buffers = True
        # XXX fixed for now because it gives different results for hair
        rd.threads_mode = 'AUTO'
        '''
        rd.threads_mode = 'FIXED'
        if ip in ("192.168.4.75", "192.168.4.76"):
            rd.threads = 4
        else:
            rd.threads = 8
        '''


        # REMOVE SOON
        '''
        if ip == "192.168.3.190":
            scene.cycles.device = 'GPU'
        '''

        if processor == 'CPU':
            scene.cycles.device = 'CPU'
            if rd.parts_x < 32:
                rd.parts_x = 32
            if rd.parts_y < 16:
                rd.parts_y = 16
        elif processor == 'CUDA':
            scene.cycles.device = 'GPU'
            # XXX, WORKAROUND FOR CYCLES
            rd.parts_x = rd.parts_y = 1
        else:
            assert(0)

        scene.cycles.use_cache = False

        print("rendering using %d threads" % (rd.threads))
        rd.use_local_coords = False
        rd.raytrace_method = 'AUTO'

        # resolution
        rd.use_border = False
        rd.image_settings.color_mode = 'RGB'
        rd.use_simplify = False

        # default width and height
        width, height = 1920, 800

        # quality
        if quality == "File settings":
            pass
        elif quality == "Preview 1K":
            rd.resolution_percentage = 50
            rd.resolution_x, rd.resolution_y = width, height

            rd.use_simplify = True
            rd.simplify_subdivision = 0
            rd.simplify_child_particles = 1.0
            rd.simplify_shadow_buffer_samples = 1
            rd.simplify_shadow_buffer_size = 512
            rd.simplify_ao_sss = 0.2
            #if scene.world:
            #    scene.world.lighting.use_cache = False
            #    scene.world.lighting.samples = 1
        elif quality == "NoShading 1K":
            rd.resolution_percentage = 50
            rd.resolution_x, rd.resolution_y = width, height

            rd.use_textures = False
            rd.use_raytracing = False
            rd.use_sss = False
            rd.use_shadows = False
        elif quality == "Simplified 1K":
            rd.resolution_percentage = 50
            rd.resolution_x, rd.resolution_y = width, height

            rd.use_textures = True
            rd.use_raytracing = False
            rd.use_sss = False
            rd.use_shadows = False

            rd.use_simplify = True
            rd.simplify_subdivision = 0
            rd.simplify_child_particles = 0.1
            #rd.simplify_mipmap_levels = 5
        elif quality == "Final 4K":
            # is this resolution right?
            rd.resolution_percentage = 200
            rd.resolution_x, rd.resolution_y = width, height
        elif quality == "Final 1K":
            rd.resolution_percentage = 50
            rd.resolution_x, rd.resolution_y = width, height
        elif quality == "Final 0.5K":
            rd.resolution_percentage = 25
            rd.resolution_x, rd.resolution_y = width, height
        elif quality == "Final HD":
            rd.resolution_percentage = 100
            rd.resolution_x, rd.resolution_y = 1920, 1080
        else:
            # this should never run really
            print("ERROR: %r not known!" % quality)
            rd.resolution_percentage = 100
            rd.resolution_x, rd.resolution_y = width, height

        scene.frame_start = render_frame
        scene.frame_end = render_frame

    print("rendering frame %d" % (render_frame))

    # TODO, 02.f.blend has this bug!
    # scene_current.frame_set(scene_current.frame_current)

    for sce_iter in bpy.data.scenes:
        sce_iter.frame_set(scene_current.frame_current)

    # run once context is entirely set
    local_register()

    if not check_footage():
        print("Some footage is missing, doing nothing")
    else:
        if fpath:
            bpy.ops.render.render(animation=True)


if __name__ == "__main__":
    main()
