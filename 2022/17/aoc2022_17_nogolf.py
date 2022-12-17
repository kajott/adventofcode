#!/usr/bin/env python3
import itertools
import sys

class AoCTetris:
    shapedef = [
        {(0,0), (1,0), (2,0), (3,0)},  # -
        {(1,0), (0,1), (1,1), (2,1), (1,2)},  # +
        {(0,0), (1,0), (2,0), (2,1), (2,2)},  # L
        {(0,0), (0,1), (0,2), (0,3)},  # |
        {(0,0), (1,0), (0,1), (1,1)},  # .
    ]

    def __init__(self, infile):
        self.jet = [{'<':-1, '>':+1}[c] for c in open(infile).read().strip()]
        self.reset()
    
    def reset(self):
        self.jetpos = 0
        self.loops = 0
        self.shapes = itertools.cycle(self.shapedef)
        self.maxy = 0
        self.miny = 0
        self.maxcol = 7 * [0]
        self.resting = {(x,-1) for x in range(7)}
        self.rocks = 0
        self.next_prune = 1000000000000
        self.newrock()

    def dump(self, title=None):
        assert all(y < self.maxy for x,y in self.resting)
        yend = self.maxy
        if self.falling:
            yend = max(yend, max(y+1 for x,y in self.falling))
        if title: print(title + ':')
        for y in range(yend-1, self.miny-1, -1):
            print('|' + ''.join(".#@?"[((x,y) in self.falling) * 2 + ((x,y) in self.resting)] for x in range(7)) + '|')
        if not self.miny: print('+-------+')
        print()

    def newrock(self):
        self.falling = {(x+2, y+self.maxy+3) for (x,y) in next(self.shapes)}

    def rock(self, verbosity=0):
        old_loops = self.loops
        self.rocks += 1
        if verbosity >= 2: self.dump(f"rock #{self.rocks} appeared")
        while True:
            # jet pushing
            dx = self.jet[self.jetpos]
            self.jetpos += 1
            if self.jetpos >= len(self.jet):
                self.jetpos = 0
                self.loops += 1
            new = {(x+dx, y) for x,y in self.falling}
            ok = all(0<=x<7 for x,y in new) and not(new & self.resting)
            if ok:
                self.falling = new
            if verbosity >= 2: self.dump("push " + {-1:"left", +1:"right"}[dx] + ("" if ok else " (nothing happens)"))

            # jet falling
            new = {(x, y-1) for x,y in self.falling}
            if self.resting & new:
                break
            self.falling = new
            if verbosity >= 2: self.dump("falling")
        self.resting |= self.falling
        self.maxy = max(self.maxy, max(y for x,y in self.falling) + 1)
        #self.maxcol = [max((y for x,y in self.resting if x==c), default=0) for c in range(7)]
        #self.maxy = max(self.maxcol) + 1
        #self.miny = min(self.maxcol) - 1000
        if self.maxy > self.next_prune:
            self.miny = self.maxy - 1000
            self.resting = {(x,y) for x,y in self.resting if (y >= self.miny)}
            self.next_prune = self.maxy + 1000
        #print(self.maxy, self.miny, self.maxcol)
        self.falling = set()
        if verbosity >= 2: self.dump(f"rock #{self.rocks} came to rest")
        self.newrock()
        if verbosity >= 1: self.dump(f"new rock (#{self.rocks+1}) appears")
        return self.loops - old_loops

    def run_rocks(self, n=1):
        r0 = self.rocks
        y0 = self.maxy
        for i in range(n):
            self.rock()
        return (self.rocks - r0, self.maxy - y0)

    def run_loops(self, n=1):
        r0 = self.rocks
        y0 = self.maxy
        while n > 0:
            n -= self.rock()
        return (self.rocks - r0, self.maxy - y0)

if __name__ == "__main__":
    t = AoCTetris(sys.argv[1] if (len(sys.argv) > 1) else "input.txt")
    
    if 1:  # Part 1
        t.reset()
        for i in range(2022): t.rock()
        assert t.rocks == 2022
        print(t.maxy)

    if 0:  # experiment towards Part 2
        t.reset()
        drlist = []
        dylist = []
        while True:
            dr, dy = t.run_loops(1)
            drlist.append(dr)
            dylist.append(dy)
            try:
                drmatch = min(n for n in range(1, len(drlist) // 2) if (drlist[-2*n:-n] == drlist[-n:]))
            except ValueError:
                drmatch = 0
            try:
                dymatch = min(n for n in range(1, len(dylist) // 2) if (dylist[-2*n:-n] == dylist[-n:]))
            except ValueError:
                dymatch = 0
            print(f"loop {t.loops:5d} | dr {dr:5d} | dy {dy:5d} | drmatch {drmatch:5d} | dymatch {dymatch:5d}")

    if 1:  # Part 2 solution
        t.reset()
        wr = 1000000000000
        wy = 0
        #print(wr, wy)

        dr, dy = t.run_loops(5)
        wr -= dr
        wy += dy
        print(f"CHECKPOINT 1: {t.rocks:13d} total  rocks, {t.maxy:13d} total height")
        print(f"              {     dr:13d} delta  rocks, {    dy:13d} delta height")
        print(f"              {     wr:13d} remain rocks, {    wy:13d} accum height")

        dr, dy = t.run_loops(5)
        div = wr // dr
        wr -= div * dr
        wy += div * dy
        print(f"CHECKPOINT 2: {t.rocks:13d} total  rocks, {t.maxy:13d} total height")
        print(f"              {     dr:13d} delta  rocks, {    dy:13d} delta height ({div} repetitions)")
        print(f"              {     wr:13d} remain rocks, {    wy:13d} accum height")

        dr, dy = t.run_rocks(wr)
        wr -= dr
        wy += dy
        print(f"CHECKPOINT 3: {t.rocks:13d} total  rocks, {t.maxy:13d} total height")
        print(f"              {     dr:13d} delta  rocks, {    dy:13d} delta height")
        print(f"              {     wr:13d} remain rocks, {    wy:13d} accum height")
        assert wr == 0
        print(wy)

    if 0:  # a failed Part 2 experiment
        t.reset()
        period = len(t.jet) * 5
        print("expected period:", period)
        dylist = []
        while True:
            r0, y0 = t.rocks, t.maxy
            for i in range(period): t.rock()
            dylist.append(t.maxy - y0)
            try:
                match = min(n for n in range(1, len(dylist) // 2) if (dylist[-2*n:-n] == dylist[-n:]))
            except ValueError:
                match = 0
            print(t.rocks - r0, t.maxy - y0, match, len(t.resting))
