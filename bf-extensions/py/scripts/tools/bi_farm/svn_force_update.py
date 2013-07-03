#!/usr/bin/python
'''
Workaround svn crappyness
run:
 python svn_force_update.py /usr/bin/svn up ...options...
'''

import os
import sys
import subprocess

filename = os.path.basename(__file__)


def main():

    args = []
    ok = False
    for arg in sys.argv:

        if ok:
            args.append(arg)

        if arg.endswith(filename):
            ok = True

    update_path = sys.path[-1]

    if not os.path.isdir(update_path):
        print("Error: %s is not a directory" % update_path)
        return

    while 1:
        # print(subprocess.Popen(["/br/blender", "--background", f, "--python", __file__], stdout=subprocess.PIPE).communicate()[1])
        # args
        print(args)
        stdout, stderr = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        stderr = stderr.decode()

        print(stdout)
        print(stderr)

        ERR = "Checksum mismatch while updating "

        if ERR in stderr:
            # svn: Checksum mismatch while updating '/d/ani/render_gl/2/2_b.avi'; expected: 'd0cd1b086167ece41e5c4d3c14d99932', actual: '5c7f26055539a84aa69a3ad9b2be61c1'\n
            error = stderr.split(ERR)[-1]
            # '/d/ani/render_gl/2/2_b.avi'; expected: 'd0cd1b086167ece41e5c4d3c14d99932', actual: '5c7f26055539a84aa69a3ad9b2be61c1'\n"
            error = error.split(";")[0]
            # '/d/ani/render_gl/2/2_b.avi'
            error = error[1:-1]
            # /d/ani/render_gl/2/2_b.avi

            error_dir = os.path.dirname(error)

            if not error_dir.startswith("/mango/") and not error_dir.startswith("/media/data/mango"):
                print("Dir '%s' is not apart of mangos svn" % error_dir)
                break
            else:
                print("Removing:", error_dir)
                os.system("rm -rf '%s'" % error_dir)

        else:
            break


if __name__ == "__main__":
    main()
