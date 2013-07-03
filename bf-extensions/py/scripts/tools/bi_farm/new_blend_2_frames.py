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

import blend_render_info
import os

from render_dirs import FARM_DIR
from render_dirs import REND_DIR

# frames/%s/%s_######" % (fname, fname)

# internal access only
def _blend_2_frames_start_end(path, start, end, step=1):
    """Negative step for absolute frame count"""
    images = []
    fname = os.path.splitext(os.path.basename(path))[0]
    assert(step != 0)

    format_string = os.path.join(REND_DIR, fname, fname + "_%.6d.exr")
    
    # negative steps means total number
    if step < 0:
        if (-step >= (end - start)):
            step = 1


    if step > 0:
        frame = start
        while frame <= end:
            images.append((frame, format_string % frame))
            frame += step        
    else:
        total = -step
        for i in range(total):
            fac = i / (total - 1)
            frame = start + int(fac * (end - start))
            images.append((frame, format_string % frame))
            

    return images


def blend_2_frames(path, step=1):
    try:
        values = blend_render_info.read_blend_rend_chunk(path)
    except IOError:
        return []

    images = []

    for start, end, scene in values:
        images += _blend_2_frames_start_end(path, start, end, step=step)

    return images


def main():
    import sys
    for arg in sys.argv[1:]:
        if arg.lower().endswith('.blend'):
            for path in blend_2_frames(arg):
                print(path)


if __name__ == '__main__':
    main()

#for frame, path in blend_2_frames(os.path.join(FARM_DIR, "/pro/comps/03.1_alley/03.1b.blend")):
#    print path
