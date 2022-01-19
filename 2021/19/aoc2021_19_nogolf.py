#!/usr/bin/env python3
import re


class vec3:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def __str__(self):
        return f"{self.x},{self.y},{self.z}"
    def __sub__(a, b):
        return vec3(a.x - b.x, a.y - b.y, a.z - b.z)
    def __add__(a, b):
        return vec3(a.x + b.x, a.y + b.y, a.z + b.z)
    def dist(a, b):
        return abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)
    def to_tuple(self, *extras):
        return (self.x, self.y, self.z, *extras)
    def __eq__(a, b):
        return (a.x == b.x) and (a.y == b.y) and (a.z == b.z)
    def __hash__(v):
        return v.x ^ (v.y << 20) ^ (v.z << 40)


class mat3:
    def __init__(self, rot):
        rot = rot % 48
        self.rot = rot
        m = [
            vec3(-1 if (rot & 2) else 1, 0, 0),
            vec3(0, -1 if (rot & 4) else 1, 0),
            vec3(0, 0, -1 if (rot & 8) else 1),
        ]
        self.x = m.pop(rot >> 4)
        self.y = m.pop(rot & 1)
        self.z = m[0]
    def __mul__(m, v):
        return vec3(m.x.x * v.x + m.x.y * v.y + m.x.z * v.z,
                    m.y.x * v.x + m.y.y * v.y + m.y.z * v.z,
                    m.z.x * v.x + m.z.y * v.y + m.z.z * v.z)
    def __str__(self):
        return f"{self.x!s};{self.y!s};{self.z!s} ({self.rot})"


class CoordinateSystem:
    def __init__(self):
        self.points = set()

    def __str__(self):
        return f"{len(self.points)} points"

    def join(self, other):
        for rot in range(48):
            m = mat3(rot)
            hist = {}
            for a in self.points:
                for b in other.points:
                    delta = a - (m * b)
                    f = hist.get(delta, 0) + 1
                    hist[delta] = f
                    if f >= 12:
                        # overlap found -> apply it
                        for p in other.points:
                            self.points.add((m * p) + delta)
                        return delta


if __name__ == "__main__":
    scanners = []
    for line in open("input.txt"):
        numbers = list(map(int, re.findall('-?\d+', line)))
        if len(numbers) == 1:
            scanners.append(CoordinateSystem())
        if len(numbers) == 3:
            scanners[-1].points.add(vec3(*numbers))

    centers = [vec3(0,0,0)]
    ib = 999
    while len(scanners) > 1:
        if ib >= len(scanners):
            ib = 1
        c = scanners[0].join(scanners[ib])
        if c:
            centers.append(c)
            del scanners[ib]
        else:
            ib += 1

    print(scanners[0])
    print("max distance:", max(a.dist(b) for a in centers for b in centers))
