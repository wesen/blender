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

# runs on a node, generates avis, last arg is dir full of exrs

import os
import time
import new_blend_2_frames
from render_dirs import FARM_DIR
from render_dirs import REND_DIR
from render_dirs import GEN_AVI_IP
from render_dirs import GEN_AVI_USER
import time


# assume guest
BIN = os.path.join(FARM_DIR, "blender_farm.sh")
SCRIPT = os.path.join(FARM_DIR, "blender_exr_to_avi.py")
# for testing, run locally rather then a command over ssh
DO_LOCAL = True


def file_date(path):
    #currtime = (year, month, day, hour, min, sec)
    # year, month, day, hour, minute, second, weekday, yearday, daylight = now
    return time.localtime(os.stat(path)[8])[0:6]


def find_file(dir, filename):
    for root, dirs, files in os.walk(dir):
        if filename in files:
            return os.path.join(root, filename)

    return None


def generate(ip, user=GEN_AVI_USER):
    frame_dir = os.path.join(REND_DIR)
    frame_dirs = os.listdir(frame_dir)
    frame_dirs.sort()

    commit_avis = []

    for fdir in frame_dirs:
        image_dir = os.path.join(frame_dir, fdir)
        if not os.path.isdir(image_dir):
            continue

        # find number of frames
        blendfile = find_file(os.path.join(FARM_DIR, "mango_svn"), fdir + ".blend")
        if not blendfile:
            continue

        #os.system("svn up %s > /dev/null" % blendfile)
        frames = new_blend_2_frames.blend_2_frames(blendfile)

        # find avis and exrs
        files = os.listdir(image_dir)

        exrs = []
        avi = None
        if fdir + ".avi" in files:
            avi = fdir + ".avi"

        for frame_nr, frame_path in frames:
            f_dir, f_fname = os.path.split(frame_path)
            if f_fname in files:
                exrs += [f_fname]

        #if len(exrs) != len([f for f in files if f.endswith(".exr")]):
        #    print("frames mismatch %s %d vs %d" % (fdir, len(exrs), len([f for f in files if f.endswith(".exr")])))

        skip = False
        if len(exrs) == 0 or len(exrs) != len(frames):
            print("frames not complete (%d/%d): %s" % (len(exrs), len(frames), image_dir))
            if avi:
                commit_avis += [(image_dir, avi)]
            skip = True
        elif avi:
            exr_date = max([file_date(os.path.join(image_dir, f)) for f in exrs])
            avi_date = file_date(os.path.join(image_dir, avi))

            commit_avis += [(image_dir, avi)]

            # avi is newer
            if avi_date > exr_date:
                print("avi up to date: %s" % image_dir)
                skip = True

        if not skip:
            cmd_local = "%s --background --python %s -- %s %s; sync" % (BIN, SCRIPT, image_dir, blendfile)
            if DO_LOCAL:
                cmd = cmd_local
            else:
                cmd = "ssh -p 22 %s@%s '%s'" % (user, ip, cmd_local)

            print(cmd)
            try:
                os.system(cmd)
            except:
                import traceback
                traceback.print_exc()

                os.system("rm %s" % os.path.join(image_dir, avi))

    # wait for nfs, sync command above also helps hopefully
    time.sleep(10)

    # disabled auto commit for now
    """
    os.system("svn up " + os.path.join(FARM_DIR, "ani/render"))

    commit_files = ""
    for dir, avi in commit_avis:
        from_file = os.path.join(dir, avi)
        to_file = os.path.join(FARM_DIR, "ani/render", avi)
        if os.path.exists(to_file):
            print(to_file, file_date(to_file))
        if os.path.exists(from_file):
            print(from_file, file_date(from_file))
        if not os.path.exists(to_file) or (os.path.exists(from_file) and file_date(from_file) > file_date(to_file)):
            print("copying " + from_file)
            os.system("cp %s %s" % (from_file, to_file))
        commit_files += " \"%s\"" % to_file

    print("committing " + commit_files)
    os.system("svn add " + commit_files)
    os.system("svn status " + commit_files)
    os.system("svn commit -m \"Updated .avi's from the farm.\" " + commit_files)
    """

if __name__ == '__main__':
    generate(GEN_AVI_IP)
