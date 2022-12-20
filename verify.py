#!/usr/bin/env python2
"""
Run all AoC solutions, verify the results, sizes and runtimes,
and update README.md accordingly.
"""
import sys, os, time, re, subprocess, argparse
import multiprocessing, threading, Queue

g_run = True
g_update_times = False
g_update = True
g_create = False

###############################################################################

def is_relevant_file(name):
    name = name.lower()
    return name.startswith("aoc") \
       and name.endswith((".py", ".c")) \
       and not("_vis" in name) \
       and not("_trace" in name) \
       and not("_test" in name) \
       and not("nogolf" in name)

LANGUAGES_INV = { "py": "Python", "c": "C" }
LANGUAGE_EXTS = dict((n.lower(), x) for x,n in LANGUAGES_INV.items())
TIME_UNITS = { "s": 1, "ms": 1E-3, "m": 60, "min": 60, "h": 3600, "hrs": 3600 }
INTERPRETERS = { "py": ["python2"], "c": ["sh"], "cpp": ["sh"] }

def log(msg):
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()
def log_info(msg):    log("\x1b[37m[INFO]\x1b[0m " + msg + "\x1b[0m")
def log_warning(msg): log("\x1b[31;1m[WARN]\x1b[0m " + msg + "\x1b[0m")
def log_error(msg):   log("\x1b[41;1;37m [ERR]\x1b[0m " + msg + "\x1b[0m")

g_exit = False

###############################################################################

time_steps = (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0)
time_scales = (
    (100, "ms"),
    (1, "s"),
    (10, "s"),
    (1, "min"),
    (10, "min"),
    (1, "h"),
    (10, "h"),
    (100, "h"),
)

def quantize_time(t):
    if t < 0.08: return (0.1, "<100 ms")
    for scale, unit in time_scales:
        unit_scale = TIME_UNITS[unit]
        for step in time_steps:
            tq = step * scale * unit_scale
            if t < tq * 1.02:
                i = int(step * scale * 10 + 0.5)
                if i % 10:
                    return (tq, "~%d.%d %s" % (i / 10, i % 10, unit))
                else:
                    return (tq, "~%d %s" % (i / 10, unit))
    return (1E6, "infinity")

###############################################################################

g_config = {}

CONFIG_STATEMENTS = {
    "ignore":     ('ignore', True),
    "nonote":     ('nonote', True),
    "bothparts":  ('part-alias', 0),
    "part1":      ('part-alias', 1),
    "part2":      ('part-alias', 2),
    "check1only": ('check-only', 1),
    "check2only": ('check-only', 2),
    "nocheck":    ('check', False),
    "norun":      ('run', False),
    "python2":    ('interpreter', ["python2"]),
    "python3":    ('interpreter', ["python3"]),
}

def load_config(basedir, filter_path=""):
    configfile = os.path.join(basedir, "verify.conf")
    try:
        f = open(configfile)
    except EnvironmentError:
        return False
    for line in f:
        line = line.split('#', 1)[0].strip()
        m = re.search(r'"([^"]*)"', line)
        if m:
            comment = m.group(1).lower()
            line = line[:m.start(0)] + line[m.end(0):]
        else:
            comment = None
        line = line.strip().split()
        if not(line) or not(line[0]):
            continue
        filename = line[0].replace('\\','/').lower()
        if not filename.startswith(filter_path):
            continue
        filename = filename[len(filter_path):]
        if not(filename in g_config):
            g_config[filename] = {}
        if comment is not None:
            g_config[filename]['comment'] = comment
        for stmt in line[1:]:
            try:
                key, value = CONFIG_STATEMENTS[stmt.lower()]
            except KeyError:
                log_error("unrecognized statement '%s' for file %s in %s" % (stmt, filename, configfile))
                key = None
            if key:
                g_config[filename][key] = value
    f.close()
    return True

###############################################################################

class Sortable(object):
    def __cmp__(self, other):
        return cmp(self.sortkey, other.sortkey)

class SolutionFile(Sortable):
    def __init__(self, root, filename):
        self.dirname = root
        self.filename = filename
        self.path = os.path.normpath(os.path.join(root, filename))
        self.config = g_config.get(self.path.replace('\\','/').lower(), {})
        filename, ext = os.path.splitext(filename.lower())
        self.lang = ext.strip('.')
        if 'part-alias' in self.config:
            self.part = self.config['part-alias']
        else:
            m = re.search('_part(\d+)($|[_.])', filename)
            self.part = int(m.group(1)) if m else 0
        self.group = (self.part, self.lang)
        self.sortkey = (self.part, self.lang, filename)
        self.note = None

    def assign(self, note):
        self.note = note
        note.file = self

    def __str__(self):
        return self.filename

class SolutionNote(Sortable):
    @classmethod
    def findall(self, readme, path="readme file"):
        return [self(m, path) for m in re.finditer(r'^\s*\*\s+parts?\s+(?P<parts>[0-9+]+),\s+(?P<lang>\w+)(\s*\((?P<comment>.*?)\))?:\s+(?P<size>\d+)\s+bytes,\s+(?P<tr>[<~])\s*(?P<tv>\d+(\.\d+)?)\s*(?P<tu>m?s|m(in)?|h(rs)?)', readme, flags=re.I+re.M)]

    def __init__(self, m, path="readme file"):
        self.raw = m.group(0).strip()
        self.parts = set(map(int, m.group('parts').split('+')))
        self.part = min(self.parts) if (len(self.parts) == 1) else 0
        lang = m.group('lang').lower()
        try:
            self.lang = LANGUAGE_EXTS[lang]
        except KeyError:
            log_warning("unrecognized language '%s' in %s" % (m.group('lang'), path))
            self.lang = lang
        self.comment = (m.group('comment') or "").lower()
        self.size = int(m.group('size'))
        self.time_rel = m.group('tr')
        try:
            scale = TIME_UNITS[m.group('tu').lower()]
        except KeyError:
            log_warning("unrecognized time unit '%s' in %s" % (m.group('tu'), path))
            scale = 1
        self.time = float(m.group('tv')) * scale
        self.rawtime = m.group('tr') + m.group('tv') + m.group('tu')
        self.pos = m.start(0)
        self.pos_size_start = m.start('size')
        self.pos_size_end = m.end('size')
        self.pos_time_start = m.start('tr')
        self.pos_time_end = m.end('tu')
        self.file = None
        self.new_size = None
        self.new_time = None
        self.group = (self.part, self.lang)
        self.sortkey = (self.part, self.lang, self.pos)

    @property
    def changed(self):
        return self.new_size or self.new_time

    def apply(self, text):
        if self.new_time:
            text = text[:self.pos_time_start] + self.new_time + text[self.pos_time_end:]
        if self.new_size:
            text = text[:self.pos_size_start] + str(self.new_size) + text[self.pos_size_end:]
        return text

    def __str__(self):
        return "* Part%s %s, .%s%s: %d bytes, ~%.1f s" % ("s" if len(self.parts) > 1 else "", '+'.join(map(str, sorted(self.parts))), self.lang, " (%s)" % self.comment if self.comment else "", self.size, self.time)

###############################################################################

def clean_result_line(line):
    return line.strip("\t\r\n()").replace(' ', '')

def get_run_result(file, lines=0, expect=None):
    # detect run configuration
    partial_check = 0
    run = file.config.get('run', True)
    check = file.config.get('check', True)
    check_only = file.config.get('check-only', 0)
    if check_only:
        if not file.part:
            partial_check = check_only
        elif file.part != check_only:
            check = False
    if partial_check:
        if expect and (partial_check <= len(expect)):
            expect = [expect[partial_check - 1]]
            lines = 1
        else:
            partial_check = 0
  
    # print status
    if not run:
        extras = " (size only)"
    elif not check:
        extras = " (without answer verification)"
    elif partial_check:
        extras = " (with partial answer verification)"
    else:
        extras = ""
    log_info("checking %s%s" % (file.path, extras))

    # prepare command line
    size = os.path.getsize(file.path)
    if not(run and g_run):
        return 0, size, True
    cmdline = file.config.get('interpreter', INTERPRETERS.get(file.lang)) + [file.filename]

    # prepare result capture and verification
    if not lines:
        lines = 1 if file.part else (len(expect) if expect else 2)
    if expect and (len(expect) != lines):
        if file.part and (lines == 1) and (file.part <= len(expect)):
            expect = [expect[file.part - 1]]
        else:
            log_error("internal error: expecting %d results, but only capturing %d" % (len(expect), lines))

    # run the program
    output = []
    t = time.time()
    try:
        proc = subprocess.Popen(cmdline, cwd=file.dirname, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in proc.stdout:
            output.append(line.rstrip())
        res = proc.wait()
        if res:
            res = "exit code %d" % res
    except EnvironmentError, e:
        res = str(e)
    t = time.time() - t

    # summarize
    if res:
        log_error("error running %s: %s" % (file.path, res))
        return 0, size, False
    if len(output) > lines:
        output = output[-lines:]
    if check and expect and (map(clean_result_line, output) != expect):
        log_error("result mismatch for %s: expected '%s', got '%s'" % (file.path, ' | '.join(expect), ' | '.join(output)))
        return t, size, False
    return t, size, output

###############################################################################

def check_dir(root, files):
    global g_exit

    # parse and sort file names
    files = [f for f in (SolutionFile(root, f) for f in files if is_relevant_file(f)) if not f.config.get('ignore')]
    if not files:
        return  # directory doesn't contain any relevant files

    # read and parse the README file (search for puzzle answers and solution notes)
    readme_path = os.path.normpath(os.path.join(root, "README.md"))
    with open(readme_path, "rb") as f:
        readme = f.read()
    answers = re.findall(r'^your puzzle answer was `([^`]+)`', readme, flags=re.I+re.M)
    if not answers:
        log_warning("directory '%s' doesn't contain any puzzle answers, ignoring" % root)
        return
    notes = SolutionNote.findall(readme, readme_path)
    create = False
    if not(notes):
        if g_create:
            log_info("creating solution notes in " + readme_path)
            create = True
        else:
            log_warning("no solution note lines found in " + readme_path)

    # match files and solution notes
    for group in set(f.group for f in files) | set(n.group for n in notes):
        if create: break

        # get a list of available files and notes first
        part, lang = group
        sub_files = sorted(f for f in files if f.group == group)
        sub_notes = sorted(n for n in notes if n.group == group)

        # remove files with specific association attributes
        i = 0
        while i < len(sub_files):
            f = sub_files[i]
            if f.config.get('nonote'):
                del sub_files[i]
                continue
            comment = f.config.get('comment')
            if comment is not None:
                matches = [j for j,n in enumerate(sub_notes) if comment in n.comment]
                if not matches:
                    log_warning("comment '%s' of file %s doesn't match any solution notes" % (comment, f.path))
                elif len(matches) > 1:
                    log_warning("comment '%s' of file %s matches multiple solution notes" % (comment, f.path))
                else:
                    f.assign(sub_notes.pop(matches.pop()))
                del sub_files[i]
                continue
            i += 1

        # resolve remaining associations
        if len(sub_files) == len(sub_notes):
            for f, n in zip(sub_files, sub_notes):
                f.assign(n)
        else:
            log_warning("can't match %d file(s) with %d solution note(s) for %s part(s) %s, .%s" % \
                       (len(sub_files), len(sub_notes), root, part or "1+2", lang) \
                       + ''.join("\n file: " + f.filename for f in sub_files) \
                       + ''.join("\n note: " + n.raw for n in sub_notes))

    # run and check the files
    changed = False
    for f in sorted(files):
        if g_exit:
            return
        t_raw, size, ok = get_run_result(f, expect=answers)
        n = f.note
        if not ok:
            continue
        if create:
            if not readme.endswith("\n"):
                readme += "\n"
            readme += "* %s, %s: %d bytes, %s\n" % ("Part %s" % f.part if f.part else "Parts 1+2", LANGUAGES_INV[f.lang], size, quantize_time(t_raw)[-1])
            changed = True
        if not n:
            continue
        if size != n.size:
            log_info("size of %s changed from %d to %d bytes" % (f.path, n.size, size))
            n.new_size = size
        if t_raw:
            t_q, t_str = quantize_time(t_raw)
            if g_update_times:
                if (t_q > (n.time * 1.1)) or (t_q < (n.time * 0.75)):
                    log_info("runtime of %s changed from %s to %s" % (f.path, n.rawtime, t_str.replace(' ', '')))
                    n.new_time = t_str
            elif (t_q > (n.time * 1.5)) or (t_q < (n.time * 0.5)):
                log_info("runtime of %s seems to be %s instead of %s" % (f.path, t_str.replace(' ', ''), n.rawtime))

    # apply the README changes
    for n in sorted(notes, key=lambda n: -n.pos):
        if n.changed:
            changed = True
            readme = n.apply(readme)
    if changed and g_update:
        log_info("updating %s" % readme_path)
        with open(readme_path, 'wb') as f:
            f.write(readme)

###############################################################################

g_queue = Queue.Queue()

class WorkerThread(threading.Thread):
    def run(self):
        global g_queue, g_exit, g_finish_count
        try:
            while not(g_exit):
                check_dir(*g_queue.get_nowait())
                g_queue.task_done()
        except KeyboardInterrupt:
            print
            log_warning("aborted by user")
            g_exit = True
        except Queue.Empty:
            pass

###############################################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-C", "--chdir", metavar="DIR",
                        help="set root directory")
    parser.add_argument("-j", "--jobs", metavar="N", type=int,
                        help="set number of cores to use [default: autodetect]")
    parser.add_argument("-n", "--no-run", action="store_true",
                        help="don't run the programs, just update the sizes (implies -j1)")
    parser.add_argument("-t", "--update-times", action="store_true",
                        help="check and update runtimes")
    parser.add_argument("-k", "--no-update", action="store_true",
                        help="don't update README.md")
    parser.add_argument("-c", "--create", action="store_true",
                        help="create solution notes from scratch where applicable (implies -t, conflicts with -n)")
    args = parser.parse_args()
    if args.no_run and args.create:
        parser.error("options -n/--no-run and -c/--create are mutually exclusive")

    # apply command-line configuration
    if args.chdir:
        try:
            os.chdir(args.chdir)
        except EnvironmentError, e:
            log_error("can not change into target directory '%s' - %s" % (args.chdir, e))
            sys.exit(1)
    jobs = args.jobs or (multiprocessing.cpu_count() / 2)
    if args.no_run:
        g_run = False
        jobs = 1
    if args.no_update:
        g_update = False
    if args.update_times:
        g_update_times = True
    if args.create:
        g_create = True

    # load configuration
    cwd = os.getcwd()
    prune = ""
    while (len(cwd) > 1) and not(load_config(cwd, prune)):
        cwd, top = os.path.split(cwd)
        prune = "%s/%s" % (top, prune)

    # create list of files to process
    log_info("collecting tasks ...")
    for root, dirs, files in os.walk('.'):
        dirs.sort()
        if "README.md" in files:
            g_queue.put((os.path.normpath(root), files))
    if g_queue.qsize() < 2:
        jobs = 1  # no need to parallelize if there's only one task to do

    # process jobs
    if jobs > 1:
        log_info("processing in %d parallel jobs ..." % jobs)
        threads = [WorkerThread() for x in xrange(jobs)]
        for t in threads:
            t.daemon = True
            t.start()
        try:
            g_queue.join()
        except KeyboardInterrupt:
            print
            log_warning("aborted by user")
            g_exit = True
        if g_exit:
            log_info("waiting for worker thread(s) to exit ...")
        else:
            g_exit = True
        for t in threads:
            t.join()
    else:
        try:
            while not g_queue.empty():
                check_dir(*g_queue.get())
        except KeyboardInterrupt:
            print
            log_warning("aborted by user")
            g_exit = True
    log_info("done.")
