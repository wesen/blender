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

import cgi
import datetime
import fcntl
import http.server
import os
import os.path
import pickle
import shutil
import subprocess
import time
import urllib

from render_dirs import FARM_DIR
from render_dirs import GEN_AVI_LOG
from render_dirs import GEN_AVI_BUSY

#FARM_DIR = "/tmp"

TOTAL_PROGRESS = "No statistics yet."
JOBS = []
SLAVES = []
JOBS_FILE = os.path.join(FARM_DIR, "jobs.pkl")
SLAVES_FILE = os.path.join(FARM_DIR, "slaves.pkl")
REPO_PATH = "/extra/ltstor/svnroot/mango"
HTTPD_IP = "192.168.3.14"
#HTTPD_IP = "127.0.0.1"
HTTPD_PORT = 8333
RESTART = False
GENERATE_AVI = False
STOP_AVI = False
MOVE_OLD_FRAMES = None
OVERVIEW_BLEND = "overview.blend"


def latest_svn_info():
    command = "svnlook youngest " + REPO_PATH
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    rev = p.communicate()[0].decode("utf-8").strip()

    if len(rev):
        logs = ""
        for i in reversed(range(max(int(rev) - 4, 0), int(rev) + 1)):
            command = "svnlook log -r%d %s" % (i, REPO_PATH)
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            log = p.communicate()[0].decode("utf-8").strip()

            logs += "[%d]: %s<br/>\n" % (i, log)

        return logs, rev
    else:
        # in case we fail to read
        return "Could not look up svn information.", "HEAD"

############################ Jobs ########################


class Job:
    priority_types = ('Low', 'Medium', 'High', 'Critical', 'Final')
    step_types = ('1', '2', '3', '5', '10',  # step option
                  '-3', '-5', '-7', '-13')   # total frame option
    quality_types = ('File settings', 'Final 4K', 'Final 2K', 'Final 1K', 'Final 0.5k', 'Final HD', 'Preview 1K', 'NoShading 1K', 'Simplified 1K')
    status_types = ('Disabled', 'In Progress', 'Done!')
    order_types = ('SEQUENTIAL', 'SPARSE')
    processor_types = ('CPU', 'CUDA') # could add openal later?

    def __init__(self, id, revision, quality, step, processor):
        self.id = id
        self.status = "Disabled"
        self.progress = "0% (0/0)"
        self.priority = "Medium"
        self.revision = revision
        self.quality = quality
        self.enabled = False
        self.stats = ""
        self.step = step
        self.order = 'SEQUENTIAL'
        self.processor = processor
        self.image_done = 0
        self.image_tot = 0

    @staticmethod
    def find(id):
        for job in JOBS:
            if job.id == id:
                return job

    @staticmethod
    def dump():
        f = open(JOBS_FILE, "wb")
        pickle.dump(JOBS, f)
        f.close()

    @staticmethod
    def load():
        global JOBS
        try:
            f = open(JOBS_FILE, "rb")
            JOBS = pickle.load(f)
            for job in JOBS:
                # these could be removed later....
                # only for restarting the farm on running jobs
                if not hasattr(job, "step"):
                    job.step = 1
                if not hasattr(job, "processor"):
                    job.processor = 'CPU'
                if not hasattr(job, "order"):
                    job.order = 'SEQUENTIAL'
            f.close()
        except IOError:
            print("No jobs file, starting with 0 jobs.")
            JOBS = []

    def sortkey(self):
        # (0 == if no jobs are done)
        # this way first priority is to get at least one frame rendering
        # from each job, this means we get an ETA
        return -self.priority_types.index(self.priority)


def job_set_enabled(id, enabled):
    # slaves executing a job will detect that it is disabled in the
    # master loop and stop rendering that job
    job = Job.find(id)
    job.enabled = enabled
    Job.dump()


def job_set_priority(id, priority):
    # changes in priority are detected in master loop
    Job.find(id).priority = priority
    Job.dump()


def job_set_quality(id, quality):
    # XXX not implemented yet
    Job.find(id).quality = quality
    Job.dump()


def job_set_step(id, step):
    # changes in priority are detected in master loop
    Job.find(id).step = step
    Job.dump()


def job_set_processor(id, processor):
    # changes in priority are detected in master loop
    Job.find(id).processor = processor
    Job.dump()


def job_set_order(id, order):
    # changes in priority are detected in master loop
    Job.find(id).order = order
    Job.dump()


def job_add(id, revision, quality, step, processor):
    # master loop will find the new job when refreshes it's jobs list in
    # the outer loop, so actually starting to render may take a while
    for job in JOBS:
        if job.id == id:  # only one job per file supported
            return

    if not id.endswith(".blend"):
        return

    if id != OVERVIEW_BLEND:
        parts = os.path.dirname(id).split("/")
        subdir = os.path.join(FARM_DIR, "mango_svn")

        for i in range(0, len(parts)):
            subdir = os.path.join(subdir, parts[i])

            if not os.path.exists(subdir):
                command = "svn up -r %s %s" % (revision, subdir)
                print(command)
                os.system(command)

        command = "svn up -r %s %s" % (revision, os.path.join(FARM_DIR, "mango_svn", id))
        print(command)
        os.system(command)

    job = Job(id, revision, quality, step, processor)
    JOBS.append(job)
    # JOBS.sort(key=lambda job: job.revision)
    Job.dump()

    if MOVE_OLD_FRAMES:
        MOVE_OLD_FRAMES(job)


def job_remove(id):
    # disabling first ensures that any slaves rendering this stop the job
    job_set_enabled(id, False)
    JOBS.remove(Job.find(id))
    Job.dump()


def get_slave_count_for_job(job):
    count = 0

    if job.processor == 'CUDA':
        for slave in SLAVES:
            if slave.enabled and slave.is_cuda:
                count += 1
    else:
        for slave in SLAVES:
            if slave.enabled:
                count += 1

    return count

def job_set_stats(job):
    import exr_header_collate
    render_times = exr_header_collate.render_times(job.id)
    if render_times:
        time_avg, time_min, time_max = render_times
        time_avg_str = str(datetime.timedelta(0, round(time_avg)))
        time_max_str = str(datetime.timedelta(0, round(time_max)))

        stats = time_avg_str + " avg, " + time_max_str + " max"

        # ETA
        remain = job.image_tot - job.image_done
        slave_count = get_slave_count_for_job(job)

        if remain != 0 and slave_count != 0:
            time_eta = remain * time_avg / slave_count
            time_eta_str = str(datetime.timedelta(0, round(time_eta)))
            stats += ', ' + time_eta_str + ' ETA'

        job.stats = stats

############################ Slaves ########################


class Slave:
    def __init__(self, id, ip, is_cuda):
        self.id = id
        self.ip = ip
        self.is_cuda = is_cuda
        self.status = "Disabled"
        self.enabled = False
        self.online = False
        self.disk_space_ok = False
        self.last_space_check = 0

    @staticmethod
    def find(id):
        for slave in SLAVES:
            if slave.id == id:
                return slave

    @staticmethod
    def dump():
        f = open(SLAVES_FILE, "wb")
        pickle.dump(SLAVES, f)
        f.close()

    @staticmethod
    def load():
        global SLAVES
        try:
            f = open(SLAVES_FILE, "rb")
            SLAVES = pickle.load(f)
            
            # can remove later!
            for slave in SLAVES:
                if not hasattr(slave, "is_cuda"):
                    slave.is_cuda = False
                if not hasattr(slave, "last_space_check"):
                    slave.last_space_check = 0
                if not hasattr(slave, "online"):
                    slave.online = False
                if not hasattr(slave, "disk_space_ok"):
                    slave.disk_space_ok = True

            f.close()
        except IOError:
            print("No slaves file, starting with 0 slaves.")
            SLAVES = []


def slave_set_enabled(id, enabled):
    # master loop will detect slave.enabled and start/stop jobs
    slave = Slave.find(id)
    slave.enabled = enabled
    Slave.dump()


def slave_add(id, ip, is_cuda):
    # master loop will detect new added slaves automatically
    for slave in SLAVES:
        if slave.ip == ip:
            return

    SLAVES.append(Slave(id, ip, is_cuda))
    SLAVES.sort(key=lambda slave: slave.id)
    Slave.dump()


def slave_remove(id):
    # master loop will keep reference and then detect that it got removed
    slave_set_enabled(id, False)
    SLAVES.remove(Slave.find(id))
    Slave.dump()

######################## Actions ##########################


def master_generate_avi():
    global GENERATE_AVI
    GENERATE_AVI = True


def master_stop_avi():
    global STOP_AVI
    STOP_AVI = True


def master_restart():
    global RESTART
    RESTART = True

######################### Server ###########################


class HHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_POST(self):
        # get arguments
        length = int(self.headers['content-length'])
        if length == 0:
            return
        command = str(self.rfile.read(length), encoding='utf8')

        # execute a statement
        if self.path == '/exec':
            print("executing", command)
            eval(command)
        # add a slave
        elif self.path == '/slave_add':
            d = urllib.parse.parse_qs(command)
            slave_add(d['id'][0],
                      d['ip'][0],
                      "is_cuda" in d,  # checkbox, only exists if pressed
                      )
        # add a job
        elif self.path == '/job_add':
            d = urllib.parse.parse_qs(command)
            if 'revision' in d:
                rev = d['revision'][0]
            else:
                rev = 'HEAD'
            job_add(d['id'][0], rev, d['quality'][0], int(d['step'][0]), d['processor'][0])

        self.send_response(http.client.SEE_OTHER)
        self.send_header("Location", "/")
        self.end_headers()

        """
        self.send_response(http.client.NO_CONTENT)
        self.send_header("Content-type", "application/octet-stream")
        self.end_headers()
        """

    def do_GET(self):
        def output(text):
            self.wfile.write(bytes(text, encoding='utf8'))

        def title(text):
            output("<h1>" + text + "</h1>\n")

        def subtitle(text):
            output("<h2>" + text + "</h2>\n")

        def section(text):
            output("<h3>" + text + "</h3>\n")

        def table_begin(*columns):
            output("<table id='table-jobs'>\n")
            output("<thead>\n")
            table_row(*columns)
            output("</thead>\n")

        def table_row(*columns):
            output("<tr>")
            for col in columns:
                output("<td>" + str(col) + "</td>")
            output("</tr>")

        def table_end():
            output("</table>\n")

        def escape_id(id):
            return id.replace('\'', '\\\'')

        def checkbox(function, id, enabled):
            if enabled:
                state = "checked"
            else:
                state = ""

            output("""<input type='checkbox' %s onchange='request("/exec", "%s(\\"%s\\", " + (this.checked? "True": "False") + ")")'>""" % (state, function, escape_id(id)))

        def dropdown(function, id, value, options):
            output("""<select onchange='request("/exec", "%s(\\"%s\\", \\"" + this.value + "\\")")'>\n""" % (function, escape_id(id)))

            for option in options:
                if value == option:
                    state = "selected"
                else:
                    state = ""
                output("\t<option %s value='%s'>%s</option>\n" % (state, option, option))

            output("</select>\n")

        def action(function, name, question):
            if question:
                output("""<button onclick='if(confirm("%s")) request("/exec", "%s")'>%s</button>""" % (question, function, name))
            else:
                output("""<button onclick='request("/exec", "%s")'>%s</button>""" % (function, name))

        def return_file(path, content_type, maxlines=0):
            self.send_response(http.client.OK)
            self.send_header("Content-type", content_type)
            self.end_headers()

            try:
                if maxlines:
                    f = open(path, 'r')
                    #f.seek(0, os.SEEK_END)
                    #f.seek(-min(f.tell(), 8096), os.SEEK_END)
                    lines = f.readlines()[-maxlines:]
                    for line in lines:
                        self.wfile.write(bytes(line, encoding='utf8'))
                    lines.reverse()
                    f.close()
                else:
                    f = open(path, 'rb')
                    shutil.copyfileobj(f, self.wfile)
                    f.close()
            except IOError:
                print("error opening file", path)
                pass

        if self.path == '/master_ui.css':
            return_file('master_ui.css', 'text/css')
        elif self.path == '/master_ui.js':
            return_file('master_ui.js', 'text/javascript')
        elif self.path == '/preview.png':
            return_file(os.path.join(FARM_DIR, 'slideshow/preview_small00001.png'), 'image/png')
        elif self.path == '/preview_big.png':
            return_file(os.path.join(FARM_DIR, 'slideshow/preview_big00001.png'), 'image/png')
        elif self.path.startswith("/logs"):
            return_file(os.path.join(FARM_DIR, self.path[1:]), 'text/plain', 1000)
        elif self.path.startswith("/progress_"):
            return_file('progressbar%s' % self.path, 'image/png')
        elif self.path.endswith('png'):
            return_file('frames/rrd/%s' % self.path, 'image/png')
        elif self.path == '/lastframe.html':
            return_file(os.path.join(FARM_DIR, 'slideshow/lastframe.html'), 'text/html')

        else:
            # headers
            self.send_response(http.client.OK)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # html begin
            output("<html><head>\n")
            output("<meta http-equiv='refresh' content=30>\n")
            output("<title>Render Farm! </title>\n")
            output("<link rel='stylesheet' href='master_ui.css' type='text/css'>\n")
            output("<script src='master_ui.js' type='text/javascript'></script>")
            output("</head><body><div id='container'>\n")

            title("Render Farm!")

            # jobs
            section("Jobs")
            table_begin("", "File", "Revision", "Quality", "Status", "Progress", "Stats", "Priority", "Step", "Processor", "Order", "")

            for job in JOBS:
                output("<tr>\n")
                output("<td id='td-toggle'>")
                checkbox('job_set_enabled', job.id, job.enabled)
                output("</td>\n")
                output("<td><span class='job-dir'>" + job.id[:11] + "</span><span class='job-file'>" + job.id[11:] + "</span></td>\n")
                output("<td>" + job.revision + "</td>\n")
                output("<td>" + job.quality + "</td>\n")
                if job.status == 'Disabled':
                        output("<td id='status-disabled'>" + job.status + "</td>\n")
                elif job.status == 'In Progress':
                        output("<td id='status-inprogress'>" + job.status + "</td>\n")
                elif job.status == 'Done!':
                        output("<td id='status-done'>" + job.status + "</td>\n")
                else:
                        output("<td>" + job.status + "</td>\n")
                output("<td class='centered'>" + job.progress + "</td>\n")
                output("<td class='centered'>" + job.stats + "</td>\n")
                output("<td>")
                dropdown('job_set_priority', job.id, job.priority, Job.priority_types)
                output("</td>\n")

                # output("<td>")
                # dropdown('job_set_step', job.id, job.step, Job.step_types)
                # output("%d" % job.step)
                output("<td>" + str(job.step) + "</td>\n")
                
                # output("<td>")
                # dropdown('job_set_processor', job.id, job.processor, Job.processor_types)
                # output("%d" % job.processor)
                # output("</td>\n")
                output("<td>" + job.processor + "</td>\n")

                output("<td>")
                dropdown('job_set_order', job.id, job.order, Job.order_types)
                output("</td>\n")

                output("<td id='td-toggle'>")
                action('job_remove(\\"%s\\")' % job.id, "X", "Are you sure you want to remove this job?")
                output("</td>\n")
                output("</tr>")

            table_end()

            output("<br/>\n")

            logs, revision = latest_svn_info()

            output("<form method='post' action='/job_add'>\n")
            output("<input name='id' value='' size='50'/>\n")
            output("<input name='latest' checked='yes' type='checkbox' onchange='this.form.revision.disabled = this.checked;'>Latest</input>\n")
            output("<input name='revision' disabled='disabled' value='%s' size='10'/>\n" % (revision,))
            output("<select name='quality'>\n")
            for option in Job.quality_types:
                if option == "File settings":
                    state = "selected"
                else:
                    state = ""
                output("\t<option %s value='%s'>%s</option>\n" % (state, option, option))
            output("</select>\n")

            output("<select name='step'>\n")
            for option in Job.step_types:
                if option == "1":
                    state = "selected"
                else:
                    state = ""
                output("\t<option %s value='%s'>%s</option>\n" % (state, option, option))
            output("</select>\n")

            output("<select name='processor'>\n")
            for option in Job.processor_types:
                if option == 'CPU':
                    state = "selected"
                else:
                    state = ""
                output("\t<option %s value='%s'>%s</option>\n" % (state, option, option))
            output("</select>\n")

            output("<input type='submit' class='job-add' value='Add Job'/>\n")
            output("</form>\n")

            output("<hr/>\n")

            # latest image
            output("<div id='latest-render'>")
            section("Latest Render")
            output("<a href='preview_big.png' target='_blank'><img src='preview.png' alt='latest render image'></a>")
            output("<br/><br/>")
            output("</div>")

            #output("<hr/>\n")

#            output("<div id='extrainfo'>\n")
            # recent commits
            output("<div id='extrainfo-recentcommits'>\n")
            section("Recent Commits")
            output(logs)
            output("</div>")

            # progress
            output("<div id='extrainfo-farmprogress'>\n")
            section("Farm Progress")
            output(TOTAL_PROGRESS)
            output("</div>")

            # monitor links
            # output("<div id='extrainfo-monitor'>\n")
            # section("Monitor")
            # output("<a href='graph.html'/>Node CPU/Memory Graphs.</a>\n")
            # output("</div>")

            output("<br><br><br><hr/>\n")

            # slaves
            section("Slaves")
            table_begin("", "Name", "IP", "Alive", "Cuda", "Status", "Since", "Logs", "")

            for slave in SLAVES:
                try:
                    busyfile = os.path.join(FARM_DIR, "./logs/%s.busy" % slave.ip)
                    secdiff = round(time.time() - os.stat(busyfile).st_mtime)
                    since = str(datetime.timedelta(0, secdiff))
                except OSError:
                    since = ""

                output("<tr>\n")
                output("<td id='td-toggle'>")
                checkbox('slave_set_enabled', slave.id, slave.enabled)
                output("</td>\n")
                output("<td>" + slave.id + "</td>\n")
                output("<td>" + slave.ip + "</td>\n")
                if slave.online:
                    if slave.disk_space_ok:
                        output("<td width=96 id=\"status-done\">Online</td>\n")
                    else:
                        output("<td width=96 id=\"status-inprogress\">Disk is Full</td>\n")
                else:
                    output("<td width=96 id=\"status-disabled\">Offline</td>\n")
                output("<td>&nbsp;" + ("&#x2611;" if slave.is_cuda else "&#x2610;")  + "</td>\n")
                if slave.status == 'Disabled':
                        output("<td style='color:red'>" + slave.status + "</td>\n")
                else:
                        output("<td>" + slave.status + "</td>\n")
                output("<td>" + since + "</td>\n")
                output("<td><a href='/logs/%s.log'>log</a></td>\n" % (slave.ip,))
                #output("<a href='%s_cpu.png'>cpu</a>\n" % (slave.ip,))
                #output("<a href='%s_mem.png'>mem</a></td>\n" % (slave.ip,))
                output("<td id='td-toggle'>")
                action('slave_remove(\\"%s\\")' % slave.id, "X", "Are you sure you want to remove this slave?")
                output("</td>\n")
                output("</tr>\n")

            table_end()

            output("<br/>\n")

            output("<form method='post' action='/slave_add'>\n")
            output("<input name='id' value='Computer X' size='25'/>\n")
            output("<input name='ip' value='192.168.1.x' size='25'/>\n")
            output("<input name='is_cuda' type='checkbox'>Cuda</input>\n")
            output("<input type='submit' value='Add Slave'/>\n")
            output("</form>\n")

            output("<hr/>\n")

            # avi's
            section("Generate AVI's")

            busyfile = os.path.join(FARM_DIR, GEN_AVI_BUSY)

            if os.path.exists(busyfile) or GENERATE_AVI:
                action('master_stop_avi()', "Stop", "")
                output("... working ...")
            else:
                action('master_generate_avi()', "Start", "")

            output(" <a href='/%s'>log</a>\n" % GEN_AVI_LOG)
            output("<br/><br/>")

            # render farm
            section("Master Controls")

            action('master_restart()', "Restart", "Are you sure?")
            output("<br/>\n")
            if RESTART:
                output("waiting to restart...<br/>")

            # html end
            output("</div></body></html>\n")

############################ Run #########################

Slave.load()
Job.load()

# temporariry compat code to add stats for existing jobs
for job in JOBS:
    if not "stats" in dir(job):
        job_set_stats(job)
    if job.id.find("span") != -1:
        job_remove(job.id)


class MasterHTTPServer(http.server.HTTPServer):
    allow_reuse_address = True

    # child processes inherit sockets, and prevent us from restarting server
    # on same port, this flag ensures the socket is closed when the parent
    # process is killed
    def socket_inherit_fix(self):
        f = self.socket.fileno()
        fcntl.fcntl(f, fcntl.F_SETFD, fcntl.fcntl(f, fcntl.F_GETFD) | fcntl.FD_CLOEXEC)

print("starting httpd at %s:%d" % (HTTPD_IP, HTTPD_PORT))
HTTPD = MasterHTTPServer((HTTPD_IP, HTTPD_PORT), HHandler)
HTTPD.socket_inherit_fix()


def update(timeout):
    starttime = time.time()
    left = timeout
    while left >= 0.0:
        print("httpd handle requests for %.2fs" % left)
        HTTPD.timeout = left
        HTTPD.handle_request()
        left = timeout - (time.time() - starttime)


def close():
    HTTPD.server_close()

if __name__ == "__main__":
    HTTPD.serve_forever()
