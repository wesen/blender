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

# This script is not essential for the running of the farm
# since it only gives preview images used by the web front end.
#
# Keep this script running in its own shell.
# it loops and sends conversion commands.

import os
import time

DIR = "/render/mango/frames"
CONVERT = "/shared/software/render_farm/slideshow/exr_to_png.sh %s %s %d > /dev/null 2> /dev/null"
PNG_FILE = "/shared/software/render_farm/slideshow/preview"
NUM_IMAGES = 2
SLEEP = 120.0

def remote_command(cmd, ip="192.168.4.71", user="guest"):
    cmd_final = "ssh -n -p 22 %s@%s 'umask 000 ; %s'" % (user, ip, cmd)
    print(cmd_final)
    os.system(cmd_final)

while 1:
    print("scanning for exr files")

    # find images to display
    exr_files = []

    for root, dirs, files in os.walk(DIR):
        # print(root, files)

        # skip old files...
        if (os.sep + "old") in root:
            continue

        for file in files:
            # print(os.path.join(root, file))
            if file.endswith('.exr'):
                name = os.path.join(root, file)
                try:
                    st = os.stat(name)
                except OSError:
                    import traceback
                    traceback.print_exc()
                    continue

                if st.st_size > 10:
                    exr_files += [(name, st.st_mtime)]

    exr_files.sort(key=lambda pair: pair[1])
    exr_files = exr_files[-NUM_IMAGES:]
    exr_files.reverse()

    # convert images
    if exr_files:
        for i in range(0, NUM_IMAGES):
            name, mtime = exr_files[0]
            print("converting big", name)
            command = CONVERT % (name, PNG_FILE + "_big" + str(i), 100)
            remote_command(command)

        for i in range(0, NUM_IMAGES):
            name, mtime = exr_files[0]
            print("converting small", name)
            command = CONVERT % (name, PNG_FILE + "_small" + str(i), 30)
            remote_command(command)
    else:
        print("Can't find any images in:", DIR)

    # sleep a while until the next up
    print("sleeping for", str(SLEEP / 60), "minutes")
    time.sleep(SLEEP)
