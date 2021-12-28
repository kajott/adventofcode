#!/usr/bin/env python3

class NumberDecoder:
    def __init__(self, patterns):
        if isinstance(patterns, str):
            patterns = patterns.split()
        self.can2pat = { ''.join(sorted(pat)): pat for pat in patterns }
        self.patterns = list(map(set, patterns))
        self.pat2num = {}
        self.num2pat = {}
        self.assign(8, 7)
        self.assign(7, 3)
        _1 = self.assign(1, 2)
        _4 = self.assign(4, 4)
        _3 = self.assign(3, 5, lambda p: p > _1)
        b = _4 - _3
        _5  = self.assign(5, 5, lambda p: p > b)
        _2  = self.assign(2, 5, lambda p: (p != _3) and (p != _5))
        c = _3 - _5
        e = _2 - _3
        _6 = self.assign(6, 6, lambda p: not(p > c))
        _9 = self.assign(9, 6, lambda p: not(p > e))
        self.assign(0, 6, lambda p: (p != _6) and (p != _9))

    def assign(self, number, length, condition=lambda dummy: True):
        found_pat = [pat for pat in self.patterns if (len(pat) == length) and condition(pat)]
        assert len(found_pat) == 1
        pat = found_pat.pop()
        canon = ''.join(sorted(pat))
        noncanon = self.can2pat[canon]
        self.pat2num[canon] = number
        self.num2pat[number] = noncanon
        return pat

    def decode(self, numbers):
        if isinstance(numbers, str):
            numbers = numbers.split()
        return int(''.join(str(self.pat2num[''.join(sorted(n))]) for n in numbers))

    def __str__(self):
        return " ".join(str(n) + "=" + self.num2pat.get(n, '?') for n in range(10))

if __name__ == "__main__":
    s = 0
    with open("input.txt") as f:
        for line in f:
            patterns, numbers = line.split('|')
            s += NumberDecoder(patterns).decode(numbers)
    print(s)
