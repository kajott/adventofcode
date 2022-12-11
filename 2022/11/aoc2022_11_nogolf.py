#!/usr/bin/env python3
from collections import deque
import re

class Monkey:
    def __init__(self, text, div=0):
        self.num = int(re.search(r'(\d+):$', text, flags=re.I+re.M).group(1))
        self.initial = [int(x.strip()) for x in re.search(r'starting items:(.*)', text, flags=re.I+re.M).group(1).split(',')]
        m = re.search(r'operation: new = old ([+*]) (\d+|old)', text, flags=re.I+re.M)
        self.op = m.group(1)
        if m.group(2) == "old":
            self.op = "2"
            self.const = 0
        else:
            self.const = int(m.group(2))
        self.mod = int(re.search(r'test: divisible by (\d+)', text, flags=re.I+re.M).group(1))
        self.targets = [-1, -1]
        for c, t in re.findall(r'if (true|false): throw to monkey (\d+)', text, flags=re.I+re.M):
            self.targets[int(c=="true")] = int(t)
        self.gmod = 0
        self.reset(div or 3)

    def reset(self, div=0):
        self.queue = deque(self.initial)
        self.div = div or self.div
        self.prev_activity = 0
        self.activity = 0

    def describe(self):
        print(f"Monkey {self.num}:")
        print(f"  Starting items:", ', '.join(str(i) for i in self.initial))
        print(f"  Operation: new = old {self.op} {self.const}")
        print(f"  Test: divisible by {self.mod}")
        print(f"    if true: throw to monkey {self.targets[1]}")
        print(f"    if false: throw to monkey {self.targets[0]}")
        print()

    def summary(self):
        print(f"Monkey {self.num}:", ', '.join(str(i) for i in self.queue) or "-", f"[{self.prev_activity} -> {self.activity} = {self.activity - self.prev_activity}]")

    def run(self, monkeys, verbose=False):
        self.prev_activity = self.activity
        while self.queue:
            self.activity += 1
            item_orig = item = self.queue.popleft()
            if   self.op == "+": item_op = item = item + self.const
            elif self.op == "*": item_op = item = item * self.const
            else:                item_op = item = item * item
            item_div = item = item // self.div
            if self.gmod:
                item = item % self.gmod
            check = int((item % self.mod) == 0)
            target = self.targets[check]
            if verbose:
                print(f"M{self.num}: {item_orig} -> {item_op} -> {item_div} -> {item} | {check}: {target}")
            monkeys[target].queue.append(item)


class Monkeys:
    def __init__(self, indata, verbose=False):
        self.monkeys = []
        for text in re.split('^Monkey', indata, flags=re.M+re.I):
            if not text.strip(): continue
            self.monkeys.append(Monkey(text))
            if verbose: self.monkeys[-1].describe()
            assert self.monkeys[-1].num == len(self.monkeys) - 1
        self.rounds = 0
        gmod = 1
        for m in self.monkeys:
            gmod *= m.mod
        for m in self.monkeys:
            m.gmod = gmod

    def run_rounds(self, rounds=1, verbosity=0):
        for r in range(rounds):
            for m in self.monkeys:
                m.run(self.monkeys, verbose=(verbosity>=2))
            self.rounds += 1
            if verbosity:
                print(f"After round {self.rounds}:")
                for m in self.monkeys:
                    m.summary()
                print()

    def reset(self, div=0):
        self.rounds = 0
        for m in self.monkeys:
            m.reset(div)

    @property
    def score(self):
        a = sorted(m.activity for m in self.monkeys)
        return a[-1] * a[-2]

    def run_part(self, div, rounds):
        self.reset(div)
        self.run_rounds(rounds)
        print(self.score)


if __name__ == "__main__":
    m = Monkeys(open("input.txt").read())
    m.run_part(3, 20)
    m.run_part(1, 10000)
