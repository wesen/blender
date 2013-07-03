#!/shared/software/python/bin/python3.2
import master_avi_gen
import os
from render_dirs import FARM_DIR
from render_dirs import GEN_AVI_BUSY

busypath = os.path.join(FARM_DIR, GEN_AVI_BUSY)

os.system("echo \"Generating avi's\" > %s" % busypath)
master_avi_gen.generate('192.168.4.71', user='guest')
os.system("rm %s" % busypath)
