#!/usr/bin/env python3
"""
Advent of Code 2019 'Intcode' interpreter with tracing.
Feature Level: 9.0 (day.part)
"""
import sys
import itertools, collections
import argparse
import fnmatch

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
        self.ip = self.last_ip = self.rb = 0
        self.inq = list(inputs)
        self.outq = []

    def rollback(self):
        self.running = False
        self.ip = self.last_ip

    def halt(self):
        self.running = False
        self.halted = True

    def send(self, *data):
        if len(data) == 1 and not isinstance(data[0], int):
            data = data[0]
        self.inq.extend(data)

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

    def run(self, *data):
        """
        send data into the output queue
        and run until next output is sent and return it,
        or None if a halt instruction occurred or the input buffer ran under
        """
        self.send(*data)
        self.running = True
        while self.running and not self.outq:
            self.step()
        if self.outq:
            return self.outq.pop(0)

    def run_all(self, *data):
        """
        send data into the output queue,
        run until the 'halt' instruction,
        and return all output values that occurred
        """
        self.send(*data)
        self.running = True
        while self.running:
            self.step()
        q = self.outq
        self.outq = []
        return q

###############################################################################

Puzzles = []
def puzzle(fn):
    Puzzles.append((fn.__name__.strip('_').replace('_', '.'), fn))
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

@puzzle
def _5_1():
    o = run_for_multiple_outputs(1)
    assert not any(o[:-1])
    print(o[-1])

@puzzle
def _5_2():
    run_for_single_output(5)

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

@puzzle
def _9_1():
    run_for_single_output(1)

@puzzle
def _9_2():
    run_for_single_output(2)

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
