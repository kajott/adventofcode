#!/usr/bin/env python3
import collections

InputFile, LongIDs = "input.txt", True
InputFile, LongIDs = "input2.txt", False


class Brick:
    def __init__(self, bid=0, *numbers):
        self.bid = bid
        self.name = f"L{bid}" if LongIDs else chr(bid + 64)
        self.x0, self.y0, self.z0, self.x1, self.y1, self.z1 = numbers
        self.supports = set()
        self.supported_by = set()
        assert self.x1 >= self.x0
        assert self.y1 >= self.y0
        assert self.z1 >= self.z0

    def __lt__(self, other):
        return self.bid < other.bid

    def move_z0(self, new_z0):
        self.z1 = new_z0 + self.z1 - self.z0
        self.z0 = new_z0

    def overlaps_xy(self, other):
        return (min(self.x1, other.x1) >= max(self.x0, other.x0)) \
           and (min(self.y1, other.y1) >= max(self.y0, other.y0))

    def __str__(self):
        s = f"{self.name}: {self.x0},{self.y0},{self.z0} ~ {self.x1},{self.y1},{self.z1}"
        if self.supports: s += "; supports " + ','.join(b.name for b in sorted(self.supports))
        if self.supported_by: s += "; supported by " + ','.join(b.name for b in sorted(self.supported_by))
        return s


def names(brickset):
    return ",".join(b.name for b in sorted(brickset))

def write_graph(blocks, mark=[]):
    blocks = sorted(blocks, reverse=True)
    with open("graph.dot", 'w') as dot:
        print("digraph aoc2023_22 {", file=dot)
        for b in blocks:
            print(b.name, " [color=red]"*(b in mark), ";", file=dot)
        for b in blocks:
            if b.supported_by:
                print(b.name, "->", ", ".join(o.name for o in b.supported_by), ";", file=dot)
        print("}", file=dot)


if __name__ == "__main__":
    print("importing input, checking for overlaps ...")
    falling = []
    overlaps = collections.defaultdict(set)
    for i, line in enumerate(open(InputFile)):
        new = Brick(i+1, *map(int, line.replace(',', ' ').replace('~', ' ').split()))
        for b in falling:
            if b.overlaps_xy(new):
                overlaps[new].add(b)
                overlaps[b].add(new)
        falling.append(new)

    print("falling bricks ...")
    resting = set()
    dbg_rlist=[]
    for b in sorted(falling, key=lambda b: b.z0):
        z = max((o.z1 for o in overlaps[b] & resting), default=0) + 1
        b.move_z0(z)
        b.falling = False
        resting.add(b)
        dbg_rlist.append([b.x0,b.y0,b.z0,b.x1,b.y1,b.z1])
    print("B",dbg_rlist)

    print("establishing support relationships ...")
    for b in resting:
        for o in overlaps[b]:
            if o.z0 == b.z1 + 1:
                b.supports.add(o)
                o.supported_by.add(b)

    print("part 1 answer:", sum(all(len(o.supported_by) > 1 for o in b.supports) for b in resting))

    max_falling = sum_falling = 0
    for check_block in resting:
        edge = {check_block}
        falling = {check_block}
        while edge:
            new = {o for b in edge for o in b.supports if all((a in falling) for a in o.supported_by)}
            falling |= new
            edge = new
        num_falling = len(falling) - 1
        sum_falling += num_falling
        if num_falling > max_falling:
            max_falling = num_falling
            max_falling_set = falling

    print("part 2 non-answer:", max_falling)
    print("part 2 answer:", sum_falling)
    write_graph(resting, max_falling_set)
