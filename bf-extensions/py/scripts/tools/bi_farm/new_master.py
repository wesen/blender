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

# TODO
# * auto-generate avis after job is done, non-blocking
# * detect crashes so it does not get stuck on these frames
# * link mango directory to mango_farm_svn on nodes
# * still using local svn to check for blend_2_frames

import gc
import os
import time
import master_ui
import random
import new_blend_2_frames
import socket
import subprocess
from render_dirs import FARM_DIR
from render_dirs import REND_DIR
from render_dirs import GEN_AVI_BUSY
from render_dirs import GEN_AVI_LOG

# render twice on some systems
USE_MULTI_JOBS = False

os.umask(000)

# cat /shared/software/render_farm/id_dsa.pub > /home/guest/.ssh/authorized_keys

jobs = []


def log_file(ip, ext="log"):
    return "%s/logs/%s.%s" % (FARM_DIR, ip, ext)


def get_user_for_ip(ip, user="guest"):

    # node exception
    ip_groups = ip.split(".")
    if int(ip_groups[-2]) >= 4 and int(ip_groups[-1]) >= 200:
        user = "root"
    elif ip == "192.168.4.14":
        user = "user"

    return user


def remote_command(ip, cmd, user="guest", passwd="guest", log=True):
    logpath = log_file(ip)

    # some ip's are using different user
    user = get_user_for_ip(ip, user)

    # add redirection
    if log:
        cmd += " >> %s 2>&1" % logpath

    # set the umask so files & dirs we create can be moved about
    cmd_final = "ssh -n -f -p 22 %s@%s 'umask 000 ; FARM_DIR=\"%s\" %s'" % (user, ip, FARM_DIR, cmd)

    if log:
        file = open(logpath, 'a+')
        fw = file.write
        fw(("\n\n" + "=" * len(cmd_final)) + "\n")
        fw("  %s\n" % time.asctime())
        fw(cmd_final + "\n")
        file.close()
        os.system("chmod 777 " + logpath)

    print("running:", cmd_final)

    os.system(cmd_final)

    print("done")


def overview_blend_files():
    svn_dir = "mango_svn/pro/scenes"
    dir = os.path.join(FARM_DIR, svn_dir)
    overview_files = []

    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith("_comp.blend"):
                overview_files += [os.path.relpath(os.path.join(root, file), FARM_DIR)]

    random.seed(1)
    random.shuffle(overview_files)

    return overview_files


def overview_modify(overview_files, id, frame):
    if frame < 0 or frame >= len(overview_files):
        print("overview frame out of range %d < %d < %d" % (0, frame, len(overview_files)))
        return "", [1]

    id = overview_files[frame]
    filename = os.path.join(FARM_DIR, "mango_svn", id)
    frames = new_blend_2_frames.blend_2_frames(filename)

    if len(frames) < 1:
        print("overview no frames for %s" % filename)
        return "", [1]

    return id, [(frames[0][0] + frames[-1][0]) // 2]


def job_images(job):
    blendfile_abs = os.path.join(FARM_DIR, "mango_svn", job.id)

    if job.id == master_ui.OVERVIEW_BLEND:
        overview_files = overview_blend_files()
        images = []

        for frame, file in enumerate(overview_files):
            id, frames = overview_modify(overview_files, file, frame)

            if id != "":
                fname_overview = os.path.splitext(os.path.basename(job.id))[0]
                fname = os.path.splitext(os.path.basename(id))[0]
                format_string = os.path.join(REND_DIR, fname_overview, fname + "_%.6d.exr")
                images.append((frame + 1, format_string % frames[0]))
    elif os.path.exists(blendfile_abs):
        images = new_blend_2_frames.blend_2_frames(blendfile_abs, step=job.step)
    else:
        images = []

    return images


def slaves_status_update():
    # set status for all slaves
    for slave in master_ui.SLAVES:
        if slave.enabled:
            slave.status = "Waiting"
        else:
            slave.status = "Disabled"

    # set slaves status based on log files
    logs = os.path.join(FARM_DIR, "logs")

    for f in sorted(os.listdir(logs)):
        if f.endswith(".busy"):
            busy_path = os.path.join(logs, f)
            ip = f.replace(".busy", "")

            for slave in master_ui.SLAVES:
                if slave.ip == ip:
                    try:
                        slave.status = open(busy_path, "r").read().strip()
                    except IOError:
                        pass


def jobs_status_update():
    total_done = 0
    total_tot = 0

    kill_non_critical = False

    # update job status based on existence of exr's
    for job in master_ui.JOBS:
        # list images for this job
        images = job_images(job)

        # see how many of these images are done
        image_done = 0
        image_tot = len(images)

        for frame, path in images:
            if os.path.exists(path):
                image_done += 1

        total_done += image_done
        total_tot += image_tot

        # if we have unfinished critical jobs, we kill non-critical ones
        if job.enabled and job.priority == "Critical":
            if image_done != len(images):
                kill_non_critical = True

        # update status
        if image_done == len(images):
            if image_done == 0:
                job.status = "No Frames"
            else:
                job.status = "Done!"
        elif not job.enabled:
            job.status = "Disabled"
        else:
            job.status = "In Progress"

        # update progress
        if image_tot == 0:
            percentage = 0.0
        else:
            percentage = float(image_done) / float(image_tot)
        job.progress = "%.0f%% (%d/%d)" % (100 * percentage, image_done, image_tot)
        job.image_done = image_done
        job.image_tot = image_tot

    # update total progress
    if total_tot == 0:
        percentage = 0.0
    else:
        percentage = float(total_done) / float(total_tot)
    master_ui.TOTAL_PROGRESS = "%.2f%% (%d/%d)" % (100 * percentage, total_done, total_tot)

    return kill_non_critical


def _sparse_shuffle(ls):
    # could use nicer algo
    # main point is first frames are first/last/mid
    import array
    check = array.array('b', [False]) * len(ls)
    permute = []
    step_fac = 1.0
    while len(permute) < len(ls):
        step = int(step_fac * len(ls))
        if step < 1:
            step = 1
        for i in range(0, len(ls), step):
            if not check[i]:
                permute.append(i)
                check[i] = 1
        step_fac *= 0.5

    ls[:] = [ls[i] for i in permute]


def job_find(slaves_state, do_finals, num_frames,
             filter_job=None):

    # get enabled jobs sorted by priority
    sorted_jobs = []

    for job in master_ui.JOBS:
        if job.enabled:
            sorted_jobs.append(job)

    # get all running jobs in a set
    running_jobs = set([slave_job for slave_job, slave_frames, slave_func_nr in slaves_state.values()])

    # sort non running jobs first
    sorted_jobs.sort(key=lambda job: (job in running_jobs, job.sortkey()))
    skipped_final = False

    r_job = None
    r_frames = []

    # get unfinished frame from sorted jobs
    for job in sorted_jobs:
        if job.priority == 'Final' and not do_finals:
            skipped_final = True
            continue

        if filter_job is None:
            pass
        elif not filter_job(job):
            continue

        # list images for this job
        images = job_images(job)

        if job.order == 'SPARSE':
            _sparse_shuffle(images)

        # find frame that is not finished yet
        for frame, path in images:
            if not os.path.exists(path):
                already_busy = False
                for slave_job, slave_frames, slave_func_nr in slaves_state.values():
                    if slave_job == job and frame in slave_frames:
                        already_busy = True

                if not already_busy and (r_job == None or r_job == job):
                    r_job = job
                    r_frames += [frame]
                    if len(r_frames) == num_frames or job.id == master_ui.OVERVIEW_BLEND:
                        return r_job, r_frames

    if skipped_final:
        return job_find(slaves_state, True, num_frames, filter_job=filter_job)

    return r_job, r_frames


def move_old_frames(job):
    def make_old(filename):
        import shutil

        dirname = os.path.dirname(filename)
        basename = os.path.basename(filename)

        old_dirname = os.path.join(dirname, "old")

        # make sure the target dir exists
        try:
            os.mkdir(old_dirname)
        except:
            pass
        os.system("chmod 777 " + old_dirname)

        old_filename = os.path.join(old_dirname, basename)

        try:
            shutil.move(filename, old_filename)
        except:
            os.system("rm -f " + filename)

    images = job_images(job)

    for frame, image in images:
        if os.path.exists(image):
            make_old(image)

master_ui.MOVE_OLD_FRAMES = move_old_frames


def is_busy(ip):
    return os.path.exists(log_file(ip, ext="busy"))


def touch_busy(ip):
    os.system("echo \"Sending command\" > %s" % log_file(ip, ext="busy"))


def clear_busy(ip):
    if os.path.exists(log_file(ip, ext="busy")):
        os.system("rm %s" % log_file(ip, ext="busy"))


def available_slaves():
    slaves = set()
    for slave in master_ui.SLAVES:
        if slave.enabled:
            slaves.add(slave)
    return slaves


def update_clear(ip, job, frame):
    touch_busy(ip)
    remote_command(ip, os.path.join(FARM_DIR, "new_node_update_clear.sh"))


def update_movie(ip, job, frame):
    # do local svn update
    # XXX disabled to avoid interrupting
    # os.system("svn revert -R %s" % os.path.join(FARM_DIR, "mango_svn"))
    # os.system("svn up -r%s %s" % (job.revision, os.path.join(FARM_DIR, "mango_svn")))

    touch_busy(ip)
    # do remote rsync
    remote_command(ip, os.path.join(FARM_DIR, "new_node_update_movie.sh") + " " + job.revision)


def update_frames(ip, job, frames):
    # print("render jobs")
    touch_busy(ip)
    FARM_DIR_LOCAL = "/media/data/mango_farm_svn"

    id = job.id
    filename = os.path.join(FARM_DIR_LOCAL, id)
    output_filename = filename

    if id == master_ui.OVERVIEW_BLEND:
        overview_files = overview_blend_files()
        id, frames = overview_modify(overview_files, id, frames[0] - 1)
        filename = os.path.join(FARM_DIR_LOCAL, id)

    frame_list = " ".join([str(f) for f in frames])

    remote_command(ip, os.path.join(FARM_DIR, "new_node_update_frames.sh") + " " + filename + " " + job.processor    + " " + output_filename + " \"" + job.quality + "\" " + frame_list)


def generate_avi():
    busypath = os.path.join(FARM_DIR, GEN_AVI_BUSY)
    logpath = os.path.join(FARM_DIR, GEN_AVI_LOG)

    if not os.path.exists(busypath):
        os.system("%s >> %s 2>&1 &" % (os.path.join(FARM_DIR, "new_gen_avi.py"), logpath))


def stop_avi():
    busypath = os.path.join(FARM_DIR, GEN_AVI_BUSY)

    os.system("killall -9 new_gen_avi.py")
    os.system("rm %s" % busypath)


def slave_check_online(slave):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    try:
        s.connect((slave.ip, 22))
        s.close()
        return True
    except:
        return False


def slave_check_disk_space(slave):
    now = time.time()
    if now - slave.last_space_check < 30 * 60:
        # check disk usage once in half of hour only
        return slave.disk_space_ok

    user = get_user_for_ip(slave.ip)

    script = os.path.join(FARM_DIR, "new_node_check_space.sh")
    ip = user + "@" + slave.ip

    print("Check disk usage for %s" % slave.ip)
    with subprocess.Popen([script, ip], stdout=subprocess.PIPE) as proc:
        stat = proc.stdout.read().decode().strip()
        slave.last_space_check = now
        return stat == "OK"

def stage_in():

    '''
    for slave in master_ui.SLAVES:
        print(slave.ip, slave.enabled)
        #remote_command(slave.ip, "free -m", log=True)
    return
    '''

    master_ui.RESTART = False

    update_funcs = [update_clear, update_movie, update_frames]

    # wait and watch for new jobs to be added, once they are, carry them out
    for slave in master_ui.SLAVES:
        clear_busy(slave.ip)
        if slave.enabled:
            update_clear(slave.ip, None, 0)

    # states are tuples of (job, frame, update func nr)
    slaves_state = {}
    slaves_prev = set()

    while not master_ui.RESTART:
        # avi generating controlled by the user
        if master_ui.STOP_AVI:
            stop_avi()
            master_ui.STOP_AVI = False
        if master_ui.GENERATE_AVI:
            generate_avi()
            master_ui.GENERATE_AVI = False

        kill_non_critical = jobs_status_update()
        master_ui.update(0.01)

        changed = False

        for slave in master_ui.SLAVES:
            slave.online = slave_check_online(slave)
            if slave.online:
                slave.disk_space_ok = slave_check_disk_space(slave)

        # add/remove available slaves
        slaves = available_slaves()

        for slave in slaves - slaves_prev:
            # new systems
            print("Adding:", slave.ip)
            slaves_state[slave.ip] = (None, 0, 0)
            changed = True

        for slave in slaves_prev - slaves:
            # removed systems
            print("Removing:", slave.ip)
            clear_busy(slave.ip)
            update_clear(slave.ip, None, 0)
            del slaves_state[slave.ip]
            changed = True

        i = 0
        for slave in slaves:
            # retrieve state
            slave_job, slave_frames, slave_func_nr = slaves_state[slave.ip]
            i += 1

            # detect if job got disabled or if another critical job takes
            # priority, and if so, stop it so other jobs can be started
            if slave_job:
                if not slave_job.enabled or (slave_job.priority != "Critical" and kill_non_critical):
                    print("Cancelling job %s on %s" % (slave_job.id, slave.ip))
                    update_clear(slave.ip, None, 0)
                    slaves_state[slave.ip] = (None, 0, 0)
                    changed = True

            # if slave is busy, do nothing
            if is_busy(slave.ip):
                print("busy: %s::%s" % (slave.ip, update_funcs[slave_func_nr - 1].__name__))
                continue

            # if slave is finished, go back to stage zero
            if slave_func_nr >= len(update_funcs):
                if slave_job:
                    master_ui.job_set_stats(slave_job)

                print("finished: %s" % slave.ip)
                slave_job = None
                slave_frames = []
                slave_func_nr = 0
                changed = True

            # find a new job
            if slave.online and slave.enabled and slave_func_nr == 0:
                do_finals = slave.ip.startswith("192.168.1.2")
                if slave.ip.startswith("192.168.4.7"):
                    if int(slave.ip.split(".")[-1]) in (75, 76):
                        num_frames = 1
                    else:
                        num_frames = 2
                elif slave.ip == "192.168.3.152":
                    num_frames = 2
                elif slave.ip == "192.168.4.14":
                    num_frames = 1
                else:
                    num_frames = 1

                # override crap above
                if not USE_MULTI_JOBS:
                    num_frames = 1

                # -------------------------------------------------------------
                # Filter function so we can choose what slave gets what job
                def is_slave_job_compat(job):
                    # test the processor
                    if job.processor == 'CPU':
                        return True
                    elif job.processor == 'CUDA':
                        return (slave.is_cuda == True)

                slave_job, slave_frames = job_find(slaves_state, do_finals, num_frames,
                                                   filter_job=is_slave_job_compat)

            if slave_job:
                # call next update function
                func = update_funcs[slave_func_nr]

                # only 4 computers allowed to update svn at
                # once, to avoid bogging down the server
                #if func == update_movie:
                #    tot_svn_update = 0
                #    for ip in slaves_state.keys():
                #        job, frame, nr = slaves_state[ip]
                #        if nr > 0 and update_funcs[nr-1] == update_movie:
                #            tot_svn_update += 1
                #
                #    if tot_svn_update >= 4:
                #        continue

                print(func.__name__, slave_func_nr, slave_job.id, slave_frames)
                func(slave.ip, slave_job, slave_frames)
                slave_func_nr += 1
                changed = True

            # update state
            slaves_state[slave.ip] = (slave_job, slave_frames, slave_func_nr)

            # update UI often
            master_ui.update(0.01)

        slaves_prev = set(slaves)
        slaves_status_update()

        if changed:
            sleeptime = 1.0
        else:
            sleeptime = 8.0

        print("sleeping %.1f..." % (sleeptime,))
        master_ui.update(sleeptime)

        gc.collect()

    print("All Done")


def clear_all():
    for slave in slaves:
        os.system("rm -rf " + log_file(slave.ip, ext="busy"))
        update_clear(slave.ip, None, 0)
        update_blender(slave.ip, None, 0)


def main():
    import time
    try:
        while 1:
            stage_in()
        #clear_all()
        # while 1:
        #     time.sleep(2)
    except KeyboardInterrupt:
        pass
    master_ui.close()

if __name__ == "__main__":
    main()
