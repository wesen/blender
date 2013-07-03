#!/usr/bin/env python

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

import os
import subprocess
import time
from render_dirs import REND_DIR

BIGNUM = 100000000.0


# copied from bpy.utils
def smpte_from_seconds(time):
    import math

    hours = minutes = seconds = frames = 0

    if time < 0:
        time = -time
        neg = "-"
    else:
        neg = ""

    if time >= 3600.0:  # hours
        hours = int(time / 3600.0)
        time = time % 3600.0
    if time >= 60.0:  # mins
        minutes = int(time / 60.0)
        time = time % 60.0

    seconds = time
    string = "%s%02dh, %02dmin, %0.1fsec" % (neg, hours, minutes, seconds)
    return string.replace("00h, ", "     ")


def format_time(file, sec, ip):
    return "%s | %s | %.2f | %s" % (file, smpte_from_seconds(sec), sec, ip)


def decode_rendertime(time_str):
    '''decodes blender rendertime from metadata'''
    time_split = time_str.split(":")
    sec = float(time_split.pop())
    if time_split:
        sec += float(time_split.pop()) * 60.0

    if time_split:
        sec += float(time_split.pop()) * 3600.0
    return sec


def file_date(path):
    #currtime = (year, month, day, hour, min, sec)
    # year, month, day, hour, minute, second, weekday, yearday, daylight = now
    return time.localtime(os.stat(path)[8])[0:6]


def update_render_times(dirname, all_rendertimes, size=(None, None)):
    dirname_full = os.path.join(REND_DIR, dirname)
    if not os.path.isdir(dirname_full):
        print("NOT A DIR:", dirname_full)
        return

    exrs = []
    time_sec_average = 0.0
    time_sec_min = BIGNUM
    time_sec_max = 0.0

    time_file = os.path.join(dirname_full, "render_times.txt")
    if os.path.exists(time_file):
        generate_timefile = False
        time_file_chtime = file_date(time_file)
    else:
        generate_timefile = True
        time_file_chtime = None

    for exr in sorted(os.listdir(dirname_full)):
        if exr.endswith(".exr"):
            # print(exr)
            exr_full = os.path.join(dirname_full, exr)
            exrs.append((exr, exr_full))

            if generate_timefile is False:
                if time_file_chtime < file_date(exr_full):
                    generate_timefile = True

    '''
    if generate_timefile:
        print("Timefile writing:", time_file)
    else:
        print("Timefile up-to-date:", time_file)
    '''

    # XXX - always generate
    if generate_timefile or True:
        file_rendertimes = []
        for exr, exr_full in exrs:
            # yay. we have exr

            out, err = subprocess.Popen(["exrheader", exr_full], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            # print(out)
            lines = str(out).split("\\n")
            lines_rtime = [l for l in lines if "RenderTime " in l]

            if lines_rtime:
                lines_rtime = [l for l in lines if "RenderTime " in l]
                lines_ip = [l for l in lines if "Note " in l]
                lines_size = [l for l in lines if "displayWindow " in l]

                # convert to time
                sec = decode_rendertime(lines_rtime[0].split()[-1].replace('"', ''))

                # ip of PC rendering
                # print(exr_full) # -- handy but annoying!
                if lines_ip and ": " in lines_ip[0]:
                    ip = lines_ip[0].split(": ", 1)[-1].replace('"', '')
                else:
                    # Missing metadata we normally write, most likely someone
                    # rendered locally to the farm. better not crash at least.
                    ip = "UNKNOWN"

                # size
                size_exr = lines_size[0].replace("(", "").replace(")", "").split()[-2:]
                size_exr = int(size_exr[0]) + 1, int(size_exr[1]) + 1

                if size != (None, None):
                    if size_exr != size:
                        print("Skipping mismatch size", size_exr, size)
                        continue

                file_rendertimes.append((exr, sec, ip))

        if file_rendertimes:
            for exr, sec, ip in file_rendertimes:
                time_sec_average += sec

                time_sec_max = max(time_sec_max, sec)
                time_sec_min = min(time_sec_min, sec)

            time_sec_average /= len(file_rendertimes)

            file_rendertimes.insert(0, (dirname_full, time_sec_average, ""))

            # write a txt to the farm
            
            # note:
            # its possible (but unlikely) that since checking the original
            # dir exists, that the dir gets removed, add paranoid check here
            # since this has happend before and brings down the whole farm.
            try:
                file_txt = open(time_file, 'w')
            except:
                file_txt = None
                print("Error: could not write to %r because..." % time_file)
                import traceback
                traceback.print_exc()

            if file_txt is not None:
                for item in file_rendertimes:
                    file_txt.write(format_time(*item) + "\n")

            print(time_file)
            all_rendertimes.append(file_rendertimes)

    if time_sec_min == BIGNUM:
        time_sec_min = 0.0

    return time_sec_average, time_sec_min, time_sec_max


def render_times(blendfile):
    dirname = blendfile.split("/")[-1].split("\\")[-1].replace(".blend", "")
    return update_render_times(dirname, [])


def main():
    all_rendertimes = []

    size = 2048, 872

    DIR = "/shared/render/"
    for dirname in sorted(os.listdir(DIR)):
        update_render_times(dirname, all_rendertimes, size=size)

    summery = os.path.join(DIR, "render_times.txt")
    print(summery)
    summery_file = open(summery, 'w')

    # first wrote totals
    summery_average_time = 0.0
    summery_total_time = 0.0
    summery_total_frames = 0

    for file_rendertimes in all_rendertimes:
        for exr, sec, ip in file_rendertimes:
            summery_total_time += sec
            summery_total_frames += 1

    if summery_total_frames:
        summery_average_time = summery_total_time / summery_total_frames
    else:
        summery_average_time = 0.0

    summery_file.write("Summery: average time %s | total time %s | total frames %d\n" % (smpte_from_seconds(summery_average_time), smpte_from_seconds(summery_total_time), summery_total_frames))

    for file_rendertimes in all_rendertimes:
        summery_file.write(format_time(*file_rendertimes[0]) + (" | frames %d\n" % (len(file_rendertimes) - 1)))


if __name__ == "__main__":
    import time
    while True:
        print("generating times...")
        main()
        time.sleep(3600)
