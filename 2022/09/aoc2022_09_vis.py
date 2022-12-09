#!/usr/bin/env python3
from PIL import Image

RopeLength = 50 #max(InterestingKnots) + 1
InterestingKnots = { 0:0, 1:0, 9:(255-RopeLength)//4 }  # { knot_number: extra_brightness }

class Knot:
    def __init__(self):
        self.x = self.y = 0
        self.visited = {(0,0)}

    @property
    def visited_count(self):
        return len(self.visited)

    def move(self, dx, dy=None):
        if isinstance(dx, str):
            dx, dy = { "U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0) }[dx]
        self.x += dx
        self.y += dy
        self.visited.add((self.x, self.y))

    def pull(self, head):
        if max(abs(self.x - head.x), abs(self.y - head.y)) < 2:
            return   # close enough to head
        self.x += (head.x > self.x) - (head.x < self.x)
        self.y += (head.y > self.y) - (head.y < self.y)
        self.visited.add((self.x, self.y))

    def getbbox(self, margin=0):
        xx = set(x for x,y in self.visited)
        yy = set(y for x,y in self.visited)
        return (
            min(xx) - margin, 
            min(yy) - margin,
            max(xx) + margin + 1,
            max(yy) + margin + 1
        )

    def draw(self, dest, line_stride, pixel_stride=1, value=1, offset=0, x0=0, y0=0):
        for x,y in self.visited:
            dest[(y - y0) * line_stride + (x - x0) * pixel_stride + offset] += value

if __name__ == "__main__":
    rope = [Knot() for i in range(RopeLength)]

    indata = open("input.txt").read().split()
    while indata:
        dir = indata.pop(0)
        for i in range(int(indata.pop(0))):
            rope[0].move(dir)
            for j in range(1, RopeLength):
                rope[j].pull(rope[j-1])

    for k in InterestingKnots:
        print(f"knot #{k:<2d} -> {rope[k].visited_count}")

    x0, y0, x1, y1 = rope[0].getbbox(1)
    sx = x1 - x0
    sy = y1 - y0
    print(f"bounding box (with margin): {x0},{y0} ... {x1},{y1} = {sx}x{sy} cells")

    img = bytearray(sx * sy)
    for k, knot in enumerate(rope):
        knot.draw(img, line_stride=sx, x0=x0, y0=y0, value=InterestingKnots.get(k,0)+1)

    try:
        from PIL import Image
        img = Image.frombytes('L', (sx, sy), bytes(img))
        img.show()
    except ImportError:
        with open("aoc2022_09_vis.pgm", 'wb') as f:
            f.write(f"P5\n{sx} {sy}\n{max(img)}\n".encode())
            f.write(img)
