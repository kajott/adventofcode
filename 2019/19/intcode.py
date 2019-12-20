#!/usr/bin/env python3
"""
Advent of Code 2019 'Intcode' interpreter with tracing.
Fully-functional ("day 9" feature level).
Includes puzzle solutions up to: 19.2 (day.part)
"""
import sys
import itertools, collections
import argparse
import fnmatch
import time

g_DefaultTracing = False
g_Code = []

def fmt_arg(x,m):
    if m == 0:     return str(x)
    if m == 1:     return "#" + str(x)
    if m == 2:     return "(" + str(x) + ")"
    else:          return "?" + str(x)
OP_COLUMN_WIDTH = 20

class Operation:
    def __init__(self, name, params=0, mem_inputs=[], mem_outputs=[], func=None, force_tracing=False):
        self.name = name
        self.params = params
        self.inputs = set(mem_inputs)
        self.outputs = set(mem_outputs)
        self.func = func
        self.force_tracing = force_tracing

class ProgramStop(Exception):
    pass

class ProgramHalted(ProgramStop):
    pass

class WaitingForInput(ProgramStop):
    pass

class Machine:
    ops = {
    # code:           "name",#arg,inputs,outputs,func
         1: Operation("add",   3, [1,2], [3],  lambda m,o,i: i[1] + i[2]),
         2: Operation("mul",   3, [1,2], [3],  lambda m,o,i: i[1] * i[2]),
         3: Operation("in",    1, [],    [1],  lambda m,o,i: m.inq.pop(0) if m.inq else m.rollback()),
         4: Operation("out",   1, [1],   [],   lambda m,o,i: m.outq.append(i[1])),
         5: Operation("jnz",   2, [1,2], [0],  lambda m,o,i: i[2] if i[1] else m.ip),
         6: Operation("jz",    2, [1,2], [0],  lambda m,o,i: m.ip if i[1] else i[2]),
         7: Operation("cmplt", 3, [1,2], [3],  lambda m,o,i: i[1] < i[2]),
         8: Operation("cmpeq", 3, [1,2], [3],  lambda m,o,i: i[1] == i[2]),
         9: Operation("arb",   1, [1],   [-1], lambda m,o,i: m.rb + i[1]),
        99: Operation("halt",  func=lambda m,o,i: m.halt()),
    }

    def __init__(self, code=None, name="", inputs=[], overrides={}, tracing=None):
        if code is None:
            code = g_Code
        if isinstance(code, dict):
            self.M = code.copy()
        else:
            self.M = collections.defaultdict(int, dict(zip(itertools.count(), code)))
        self.M.update(overrides)
        self.prefix = ("<{}> ".format(name)) if name else ""
        self.running = True
        self.halted = False
        self.tracing = g_DefaultTracing if (tracing is None) else tracing
        self.reset()
        self.inq = list(inputs)

    def reset(self):
        self.ip = self.last_ip = self.rb = 0
        self.inq = []
        self.outq = []

    def rollback(self):
        self.running = False
        self.ip = self.last_ip

    def halt(self):
        self.running = False
        self.halted = True

    def step(self):
        try:
            opcode = self.M[self.ip]
            op = self.ops[opcode % 100]
        except KeyError:
            op = Operation("#INV", func=lambda m,o,i: m.halt(), force_tracing=True)

        p_mode = list(map(int, str(opcode)))[-2::-1] + [0] * (op.params + 2)
        p_raw = [self.M[self.ip + i] for i in range(op.params + 1)]
        p_addr = [((self.rb + r) if (m == 2) else r) for r, m in zip(p_raw, p_mode)]
        p_val = [(a if (m == 1) else self.M[a]) for a, m in zip(p_addr, p_mode)]

        if self.tracing or op.force_tracing:
            line = "{}{:04d}: {:05d} > {:<5s} {}".format \
                   (self.prefix, self.ip, opcode, op.name,
                    ", ".join(fmt_arg(r, m) for r, m in zip(p_raw[1:], p_mode[1:])).ljust(OP_COLUMN_WIDTH))

        self.last_ip = self.ip
        self.ip += op.params + 1
        orig_ip = self.ip
        orig_rb = self.rb

        res = op.func(self, op, [(v if (i in op.inputs) else r) for r, v, i in zip(p_raw, p_val, range(op.params + 1))])

        if (res is not None) and self.running:
            if isinstance(res, (int, bool)):
                res = [res]
            for i, v in zip(sorted(op.outputs), res):
                v = int(v)
                if i > 0:
                    self.M[p_addr[i]] = v
                elif i == 0:
                    self.ip = v
                else:  # i < 0: RB
                    self.rb = v

        if self.tracing or op.force_tracing:
            for i in range(1, op.params + 1):
                if ((i in op.inputs) and (p_mode[i] != 1)) or (i in op.outputs):
                    line += " | {}: {}".format(p_addr[i], p_val[i])
                if i in op.outputs:
                    line += " -> {}".format(self.M[p_addr[i]])
            if 0 in op.outputs:
                if self.ip == orig_ip:
                    line += " | ip: unchanged"
                else:
                    line += " | ip: {} -> {}".format(orig_ip, self.ip)
            if -1 in op.outputs:
                line += " | rb: {} -> {}".format(orig_rb, self.rb)
            print(line.rstrip(), file=sys.stderr)

    def send(self, *data):
        if len(data) == 1 and not isinstance(data[0], int):
            data = data[0]
        self.inq.extend(data)
        self.running = True

    def run(self, *data):
        """
        send data into the output queue
        and run until next output is sent and return it,
        or None if a halt instruction occurred or the input buffer ran under
        """
        self.send(*data)
        while self.running and not self.outq:
            self.step()
        if self.outq:
            return self.outq.pop(0)

    def run_all(self, *data):
        """
        send data into the output queue,
        run until the 'halt' instruction or input buffer overflow,
        and return all output values that occurred
        """
        self.send(*data)
        while self.running:
            self.step()
        q = self.outq
        self.outq = []
        return q

    def recv(self, n=0):
        """
        high-level API similar to run():
        run until 'n' values have been output and return them
        (if n==0, return a scalar, else a list),
        but on 'halt' or input buffer underrun, an exception is thrown
        """
        while self.running:
            if n:
                if len(self.outq) >= n:
                    res = self.outq[:n]
                    del self.outq[:n]
                    return res
            else:
                if self.outq:
                    return self.outq.pop(0)
            self.step()
        if self.halted:
            raise ProgramHalted
        else:
            raise WaitingForInput

###############################################################################

_console_init_done = (sys.platform != 'win32')
def console_init():
    global _console_init_done
    if _console_init_done: return
    _console_init_done = True
    try:
        import ctypes
        stdout = ctypes.c_int(ctypes.windll.kernel32.GetStdHandle(ctypes.c_int(-11)))
        mode = ctypes.c_int(0)
        ctypes.windll.kernel32.GetConsoleMode(stdout, ctypes.byref(mode))
        ctypes.windll.kernel32.SetConsoleMode(stdout, ctypes.c_int(mode.value | 4))
    except Exception as e:
        print("warning: could not set up console - {}".format(e), file=sys.stderr)

def cls(flush=False):
    console_init()
    sys.stdout.write("\x1b[2J")
    if flush: sys.stdout.flush()

def clr(flush=False):
    sys.stdout.write("\x1b[K")
    if flush: sys.stdout.flush()

def cursor(show, flush=False):
    sys.stdout.write("\x1b[?25h" if show else "\x1b[?25l")
    if flush: sys.stdout.flush()

def locate(x, y=None, s="", flush=False):
    if y is None:
        y = int(x.imag)
        x = int(x.real)
    sys.stdout.write("\x1b[{};{}H{}".format(y+1, x+1, s))
    if flush: sys.stdout.flush()

###############################################################################

Puzzles = []
def puzzle(fn):
    Puzzles.append((fn.__name__.strip('_').replace('_vis', '-vis').replace('_', '.', 1).replace('_', '-'), fn))
    return fn

def run_for_single_output(*inputs):
    m = Machine(inputs=inputs)
    r = m.run()
    assert m.run() is None
    print(r)

def run_for_multiple_outputs(*inputs):
    m = Machine(inputs=inputs)
    r = m.run_all()
    assert m.halted
    return r

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@puzzle
def _2_1():
    m = Machine(overrides={1:12, 2:2})
    assert m.run() is None
    print(m.M[0])

@puzzle
def _2_2():
    for nv in range(10000):
        m = Machine(overrides={1:nv//100, 2:nv%100})
        assert m.run() is None
        if m.M[0] == 19690720:
            print(nv)
            break

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@puzzle
def _5_1():
    o = run_for_multiple_outputs(1)
    assert not any(o[:-1])
    print(o[-1])

@puzzle
def _5_2():
    run_for_single_output(5)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@puzzle
def _7_1():
    def test(phases):
        x = 0
        for name, phase in zip("ABCDE", phases):
            x = Machine(inputs=[phase, x], name=name).run()
        return x
    print(max(map(test, itertools.permutations(range(5)))))

@puzzle
def _7_2():
    def test(phases):
        machines = [Machine(inputs=[phase], name=name) for name, phase in zip("ABCDE", phases)]
        x = 0
        for m in itertools.cycle(machines):
            r = m.run(x)
            if r is None:
                break
            x = r
        return x
    print(max(map(test, itertools.permutations(range(5,10)))))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@puzzle
def _9_1():
    run_for_single_output(1)

@puzzle
def _9_2():
    run_for_single_output(2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def robowalk(init):
    "day 11 robot walk simulation"
    m = Machine()
    grid = {0:init}
    pos = 0
    heading = -1j
    try:
        while True:
            m.send(grid.get(pos, 0))
            grid[pos] = m.recv()
            heading *= 1j if m.recv() else -1j
            pos += heading
    except ProgramHalted:
        return grid

@puzzle
def _11_1():
    print(len(robowalk(0)))

@puzzle
def _11_2():
    grid = robowalk(1)
    xx = [int(p.real) for p, c in grid.items() if c]
    yy = [int(p.imag) for p, c in grid.items() if c]
    for y in range(min(yy), max(yy)+1):
        print(''.join(" #"[grid.get(x+y*1j, 0)] for x in range(min(xx), max(xx)+1)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@puzzle
def _13_1():
    m = Machine()
    grid = {}
    try:
        while True:
            x, y, t = m.recv(3)
            grid[x+y*1j] = t
    except ProgramHalted:
        pass
    print(sum(t==2 for t in grid.values()))

@puzzle
def _13_2(vis=False):
    m = Machine(overrides={0:2})
    if vis: cls(); cursor(False)
    ball = 0
    paddle = 0
    score = 0
    while True:
        try:
            x, y, t = m.recv(3)
            if   x  < 0: score  = t
            elif t == 3: paddle = x
            elif t == 4: ball   = x
            if vis:
                if x < 0:
                    locate(0, 21, t, flush=True)
                else:
                    locate(x*2, y, "  ##[]==()"[t*2:t*2+2], flush=True)
        except WaitingForInput:
            m.send((paddle < ball) - (paddle > ball))
        except ProgramHalted:
            break
    if vis:
        locate(0, 21); cursor(True)
    else:
        print(score)

@puzzle
def _13_2_vis():
    return _13_2(True)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Droid15:
    delta = [0, -1j, 1j, -1, 1]
    revdir = [0, 2, 1, 4, 3]
    range_x = list(range(41))
    range_y = list(range(41))
    start = 21 + 21 * 1j
    
    def __init__(self, vis):
        self.m = Machine()
        self.grid = collections.defaultdict(int, {self.start:2})
        self.pos = self.start
        self.target = None
        self.path = [0]
        self.vis = vis

    def dump(self, overlay={}):
        for y in self.range_y:
            line = ""
            for x in self.range_x:
                p = x+y*1j
                if p in overlay:
                    line += str(overlay[p])[-1]
                elif p == self.pos:
                    line += "X"
                else:
                    line += "?#.S"[self.grid[p]]
            print(line)

    def go(self, d):
        npos = self.pos + self.delta[d]
        res = self.m.run(d)
        assert res is not None
        self.grid[npos] = res + 1
        if res:
            if self.vis:
                time.sleep(0.001)
                locate(self.pos, s=".")
                locate(npos, s="X")
                locate(0, 41, flush=True)
            self.pos = npos
            if d == self.revdir[self.path[-1]]:
                self.path.pop()
            else:
                self.path.append(d)
        elif self.vis:
            locate(npos, s="#", flush=True)
        if res == 2:
            self.target = npos
        return res

    def explore(self):
        if 0:
            self.dump()
        come_from = self.revdir[self.path[-1]]
        for d in (1,3,2,4):
            if (d == come_from) or (self.grid[self.pos + self.delta[d]] == 1):
                continue
            if self.go(d):
                self.explore()
        if come_from:
            self.go(come_from)

    def bfs(self, start_at=None, stop_at=None):
        next = { start_at if (start_at is not None) else self.start }
        dist = 0
        visited = {}
        while next:
            curr = next
            next = set()
            dist += 1
            for oldpos in curr:
                visited[oldpos] = dist - 1
                for d in self.delta[1:]:
                    newpos = oldpos + d
                    if newpos in visited:
                        continue
                    if newpos == stop_at:
                        return dist
                    if self.grid[newpos] != 1:
                        next.add(newpos)
        return dist - 1

@puzzle
def _15(vis=False):
    droid = Droid15(vis)
    if vis: cls(); cursor(False)
    droid.explore()
    if vis: locate(0,41); cursor(True)
    else:   droid.dump()
    assert droid.target
    print(droid.bfs(stop_at=droid.target))
    print(droid.bfs(start_at=droid.target))

@puzzle
def _15_vis():
    return _15(True)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@puzzle
def _17_1():
    ascii = ''.join(map(chr, run_for_multiple_outputs()))
    print(ascii)
    grid = ascii.strip().split('\n')
    align = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[y])-1):
            if grid[y-1][x] + grid[y][x-1:x+2] + grid[y+1][x] == "#####":
                align += x * y
    print(align)

@puzzle
def _17_2():
    m = Machine(overrides={0:2})
    ascii = ''.join(map(chr, m.run_all()))
    sys.stdout.write(ascii)

    # turn grid into sparse map
    grid = set()
    pos = None
    heading = None
    for y, line in enumerate(ascii.strip().split('\n')):
        for x, cell in enumerate(line):
            p = x+y*1j
            if cell != '.': grid.add(p)
            if cell == '^': pos = p; heading = -1j
            if cell == 'v': pos = p; heading =  1j
            if cell == '<': pos = p; heading = -1
            if cell == '>': pos = p; heading =  1

    # construct walking path
    path = []
    turn = None
    walk = 0
    while True:
        if (pos + heading) in grid:
            walk += 1
            pos += heading
        else:
            if walk:
                path.append(turn + str(walk))
            walk = 0
            if (pos + heading * 1j) in grid:
                turn = "R,"
                heading *= 1j
            elif (pos - heading * 1j) in grid:
                turn = "L,"
                heading *= -1j
            else:
                break  # end of path reached
    #print(path)

    # compress walking path
    def compress(done, remain, funcs):
        if not(remain) and (len(funcs) == 3):
            return (done, funcs)  # we made it!
        if len(done) >= 10:
            return  # main program too long -> fail

        # try to apply existing functions first
        for i,f in enumerate(funcs):
            l = len(f)
            if remain[:l] == f:
                #print("FUNCTION-MATCH", i, l)
                r = compress(done + [i], remain[l:], funcs)
                if r: return r
    
        if len(funcs) >= 3:
            return  # can't use existing function, can't create new one -> fail!
    
        # otherwise build new functions
        l = 0
        while sum(map(len, remain[:l+1])) + l <= 20:
            l += 1
            #print("NEW-FUNC", len(funcs), l)
            r = compress(done + [len(funcs)], remain[l:], funcs + [remain[:l]])
            if r: return r

    prog, funcs = compress([], path, [])
    recon = []
    for f in prog: recon.extend(funcs[f])
    assert recon == path

    res = None
    for line in [','.join("ABC"[f] for f in prog)] + [','.join(f) for f in funcs] + ['n']:
        print(line)
        assert len(line) <= 20
        outdata = m.run_all(map(ord, line + "\n"))
        if outdata and (outdata[-1] > 255):
            res = outdata.pop()
        sys.stdout.write(''.join(map(chr, outdata)))
    print(res)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@puzzle
def _19_1():
    m = Machine()
    s = 0
    for y in range(50):
        line = ""
        for x in range(50):
            line += ".#"[Machine().run(x, y)]
        s += line.count('#')
        print(line)
    print(s)

class BeamSampler:
    def __init__(self):
        self.y0_ref = 1
        self.y0_slope = 0
        self.y1_ref = 1
        self.y1_slope = 9
    def get_upper(self, x):
        y = self.y0_slope * x // self.y0_ref
        while Machine().run(x, y):
            y -= 1
        while not Machine().run(x, y):
            y += 1
        if x > self.y0_ref:
            self.y0_ref = x
            self.y0_slope = y
        return y
    def get_lower(self, x):
        y = self.y1_slope * x // self.y1_ref
        while not Machine().run(x, y):
            y -= 1
        while Machine().run(x, y):
            y += 1
        if x > self.y1_ref:
            self.y1_ref = x
            self.y1_slope = y
        return y
    def get_column(self, x):
        return self.get_upper(x), self.get_lower(x)
    def fits_square(self, x, size=100):
        y = self.get_upper(x + size - 1)
        if Machine().run(x, y + size - 1):
            return y

@puzzle
def _19_2():
    s = BeamSampler()
    s.get_column(10)

    x = 0
    while not s.fits_square(x + 100): x += 100
    while not s.fits_square(x + 10): x += 10

    y = 0
    while not y:
        x += 1
        y = s.fits_square(x)
    print(x*10000+y)

###############################################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzles", metavar="PUZZLE", nargs='*',
                        help="select a puzzle to solve (choices: {})".format(', '.join(n for n,f in Puzzles)))
    parser.add_argument("-f", "--file", metavar="FILE", default="input.txt",
                        help="intcode file to run")
    parser.add_argument("-i", "--inputs", metavar="VALUES",
                        help="input values to use")
    parser.add_argument("-v", "--verbose", action='store_true',
                        help="trace execution even if running a puzzle")
    parser.add_argument("-q", "--quiet", action='store_true',
                        help="don't trace execution")
    parser.add_argument("--vn", metavar="NOUN,VERB",
                        help="initial values of memory locations 1 and 2")
    args = parser.parse_args()

    g_DefaultTracing = bool(args.verbose)
    g_Code = list(map(int, open(args.file).read().replace(',', ' ').split()))

    if args.puzzles:
        ok = False
        for name, fn in Puzzles:
            if any(fnmatch.fnmatch(name, pat) for pat in args.puzzles):
                ok = True
                fn()
        if not ok:
            parser.error("no matching puzzle")
    else:
        m = Machine(
            inputs = map(int, args.inputs.replace(',', ' ').split()) if args.inputs else [],
            overrides = dict(zip(itertools.count(1), map(int, args.vn.replace(',', ' ').split()))) if args.vn else {},
            tracing = g_DefaultTracing or not(args.quiet),
        )
        have_out = False
        while True:
            out = m.run()
            if out is not None:
                print(out)
                have_out = True
            elif m.halted:
                if not have_out:
                    print("M[0] =", m.M[0])
                break
            else:
                print("Input queue underflow.")
                break
