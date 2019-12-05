#!/usr/bin/env python3
"""
Advent of Code 2019 'Intcode' interpreter with tracing.
Feature Level: 5.2 (day.part)
"""
import sys
import itertools, collections
import argparse

def fmt_addr(x):   return "{:5d}".format(x)
def fmt_data(x):   return "{:10d}".format(x)
def fmt_marg(x):   return "{:6d}".format(x)
def fmt_larg(x):   return "#{}".format(x).rjust(6)
def fmt_opcode(x): return "{:05d}".format(x)
def fmt_opname(x): return "{:<5s}".format(x)

LONGEST_ARG = 6
MAX_NUM_ARGS = 3
OP_COLUMN_WIDTH = LONGEST_ARG * MAX_NUM_ARGS + 2 * (MAX_NUM_ARGS - 1)


class Operation:
    def __init__(self, name, params=0, mem_inputs=[], mem_outputs=[], func=None):
        self.name = name
        self.params = params
        self.inputs = set(mem_inputs)
        self.outputs = set(mem_outputs)
        self.func = func


class Machine:
    ops = {
         1: Operation("add",   3, [1,2], [3], lambda m,o,i: i[1] + i[2]),
         2: Operation("mul",   3, [1,2], [3], lambda m,o,i: i[1] * i[2]),
         3: Operation("in",    1, [],    [1], lambda m,o,i: int(input())),
         4: Operation("out",   1, [1],   [],  lambda m,o,i: print(i[1])),
         5: Operation("jnz",   2, [1,2], [0], lambda m,o,i: i[2] if i[1] else m.ip),
         6: Operation("jz",    2, [1,2], [0], lambda m,o,i: m.ip if i[1] else i[2]),
         7: Operation("cmplt", 3, [1,2], [3], lambda m,o,i: i[1] < i[2]),
         8: Operation("cmpeq", 3, [1,2], [3], lambda m,o,i: i[1] == i[2]),
        99: Operation("stop",  func=lambda m,o,i: m.stop()),
    }

    def __init__(self, code, noun=None, verb=None):
        if isinstance(code, dict):
            self.M = code.copy()
        else:
            self.M = collections.defaultdict(int, dict(zip(itertools.count(), code)))
        if noun is not None: self.M[1] = noun
        if verb is not None: self.M[2] = verb
        self.running = True
        self.ip = 0

    def stop(self):
        self.running = False

    def step(self):
        try:
            opcode = self.M[self.ip]
            op = self.ops[opcode % 100]
        except KeyError:
            op = Operation("#INV", func=lambda m,o,i: m.stop())
        digits = list(map(int, str(opcode)))[::-1] + [0] * (op.params + 2)

        raw_args = [self.M[self.ip + i] for i in range(op.params + 1)]
        mem_args = [(a if (not(i) or digits[i+1]) else self.M[a]) for i, a in enumerate(raw_args)]

        line = fmt_addr(self.ip) + ": " \
             + fmt_opcode(opcode) + " > " \
             + fmt_opname(op.name) + " " \
             + ", ".join(fmt_larg(a) if l else fmt_marg(a) for a,l in zip(raw_args[1:], digits[2:])).ljust(OP_COLUMN_WIDTH)

        inputs = [(m if (i in op.inputs) else r) for r,m,i in zip(raw_args, mem_args, range(op.params + 1))]

        self.ip += op.params + 1
        res = op.func(self, op, inputs)

        if res is not None:
            if isinstance(res, (int, bool)):
                res = [res]
            for i, v in zip(sorted(op.outputs), res):
                if i:
                    self.M[raw_args[i]] = int(v)
                else:
                    self.ip = int(v)

        for i in range(1, op.params + 1):
            if ((i in op.inputs) and not digits[i+1]) or (i in op.outputs):
                line += " | " + fmt_addr(raw_args[i]) + ": " + fmt_data(mem_args[i])
            if i in op.outputs:
                line += " -> " + fmt_data(self.M[raw_args[i]])
        if 0 in op.outputs:
            line += " | new ip: " + fmt_addr(self.ip)

        print(line, file=sys.stderr)

    def run(self):
        self.running = True
        while self.running:
            self.step()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", metavar="FILE", default="input.txt",
                        help="input intcode file")
    parser.add_argument("args", metavar="NOUN+VERB", type=int, nargs='?',
                        help="input noun and verb (2 digits each)")
    args = parser.parse_args()

    code = list(map(int, open(args.input).read().replace(',', ' ').split()))
    if args.args is not None:
        m = Machine(code, args.args // 100, args.args % 100)
    else:
        m = Machine(code)
    m.run()
