#!/usr/bin/env python3
"""
Advent of Code 2019 'Intcode' interpreter with tracing.
"""
import itertools, collections
import argparse

def fmt_addr(x): return "{:4d}".format(x)
def fmt_data(x): return "{:10d}".format(x)
def fmt_opcode(x): return "{:2d}".format(x)
def fmt_opname(x): return "{:<4s}".format(x)


class Operation:
    def __init__(self, name, params=0, mem_inputs=[], mem_outputs=[], func=None):
        self.name = name
        self.params = params
        self.inputs = set(mem_inputs)
        self.outputs = set(mem_outputs)
        self.func = func


class Machine:
    ops = {
         1: Operation("add",  3, [1,2], [3], lambda m,o,i: i[1] + i[2]),
         2: Operation("mul",  3, [1,2], [3], lambda m,o,i: i[1] * i[2]),
        99: Operation("stop", func=lambda m,o,i: m.stop()),
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
            op = self.ops[self.M[self.ip]]
        except KeyError:
            op = Operation("#INV", func=lambda m,o,i: m.stop())

        raw_args = [self.M[self.ip + i] for i in range(op.params + 1)]
        mem_args = [self.M[a] for a in raw_args]

        line = fmt_addr(self.ip) + ": " \
             + fmt_opcode(self.M[self.ip]) + " > " \
             + fmt_opname(op.name) + " " \
             + ", ".join(map(fmt_addr, raw_args[1:])).ljust(op.params * 4 + (op.params - 1) * 2)

        inputs = [(m if (i in op.inputs) else r) for r,m,i in zip(raw_args, mem_args, range(op.params + 1))]

        self.ip += op.params + 1
        res = op.func(self, op, inputs)

        if res is not None:
            if isinstance(res, int):
                res = [res]
            for i, v in zip(sorted(op.outputs), res):
                if i:
                    self.M[raw_args[i]] = v
                else:
                    self.ip = v

        for i in range(1, op.params + 1):
            if (i in op.inputs) or (i in op.outputs):
                line += " | " + fmt_addr(raw_args[i]) + ": " + fmt_data(mem_args[i])
            if i in op.outputs:
                line += " -> " + fmt_data(self.M[raw_args[i]])
        if 0 in op.outputs:
            line += " | new ip: " + fmt_addr(self.ip)

        print(line)

    def run(self):
        self.running = True
        while self.running:
            self.step()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", metavar="FILE", default="input.txt",
                        help="input intcode file")
    parser.add_argument("args", metavar="NOUN+VERB", type=int, nargs='?', default=1202,
                        help="input noun and verb (2 digits each)")
    args = parser.parse_args()

    code = list(map(int, open(args.input).read().replace(',', ' ').split()))
    m = Machine(code, args.args // 100, args.args % 100)
    m.run()
