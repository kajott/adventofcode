#!/usr/bin/env python3
import itertools


class Point:
    def __init__(self, x, y=None):
        if isinstance(x, Point):
            self.x, self.y = x.x, x.y
        if isinstance(x, str) and (',' in x) and (y is None):
            self.x, self.y = map(int, x.split(','))
        else:
            self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Box:
    def __init__(self, a: Point, b: Point):
        self.a = Point(min(a.x, b.x), min(a.y, b.y))
        self.b = Point(max(a.x, b.x), max(a.y, b.y))
        self.area = (self.b.x - self.a.x + 1) * (self.b.y - self.a.y + 1)

    def __gt__(self, other: 'Box') -> bool:
        return self.area > other.area

    def __repr__(self):
        return f"Box({self.a!r}, {self.b!r})"

class NullBox(Box):
    def __init__(self):
        self.a = Point(0,0)
        self.b = Point(0,0)
        self.area = 0


class Polygon:
    def __init__(self, points):
        self.points = list(map(Point, points))
        self.xmin = min(p.x for p in self.points)
        self.ymin = min(p.y for p in self.points)
        self.xmax = max(p.x for p in self.points)
        self.ymax = max(p.y for p in self.points)

    def iterpath(self):
        for i in range(len(self.points)):
            yield self.points[i-1], self.points[i]

    def iterboxes(self):
        for a, b in itertools.combinations(self.points, 2):
            yield Box(a, b)

    def intersects(self, box: Box) -> bool:
        rc_y = (box.a.y + box.b.y) // 2
        rc_count = 0
        for a, b in self.iterpath():
            if a.x == b.x:  # vertical edge
                u, d = min(a.y, b.y), max(a.y, b.y)  # up/down
                if u <= rc_y <= d:  # raycasting check (not needed for the solution!)
                    rc_count += 1
                if box.a.x < a.x < box.b.x:  # edge is within the box
                    if (u < box.b.y) and (d > box.a.y):  # line crosses the box
                        return True
            else:  # horizontal edge
                l, r = min(a.x, b.x), max(a.x, b.x)  # left/right
                if box.a.y < a.y < box.b.y:  # edge is withing the box
                    if (l < box.b.x) and (r > box.a.y):  # line crosses the box
                        return True
        return bool(rc_count & 1)


class SVGVisualization:
    def __init__(self, filename: str, poly: Polygon):
        self.f = open(filename, 'w')
        xmax = poly.xmax + poly.xmin
        ymax = poly.ymax + poly.ymin
        self.reduce = max(max(xmax, ymax) // 1000, 1)
        self.scale = 1.0 / self.reduce
        self.f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        self.f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{int(xmax*self.scale+1)}" height="{int(ymax*self.scale+1)}">\n')
        self.f.write(f'<g transform="scale({self.scale})">\n')
        main_path = " L ".join(f'{p.x} {p.y}' for p in poly.points)
        self.f.write(f'<path d="M {main_path} Z" stroke="#444" fill="#ccc" stroke-width="{self.reduce}" />\n')

    def box(self, box: Box, color: str = "red"):
        self.f.write(f'<rect x="{box.a.x}" y="{box.a.y}" width="{box.b.x-box.a.x}" height="{box.b.y-box.a.y}" stroke="{color}" fill="none" stroke-width="{self.reduce}" />\n')

    def __sel__(self):
        self.f.write(f'</g></svg>\n')
        self.f.close()


def solve(inputfile: str, visfile: str|None = None, expect: tuple|None = None):
    poly = Polygon(open(inputfile))
    if visfile:
        vis = SVGVisualization(visfile, poly)

    part1 = NullBox()
    part2 = NullBox()
    for box in poly.iterboxes():
        if box > part1:
            part1 = box
        if (box > part2) and not(poly.intersects(box)):
            part2 = box

    if visfile:
        vis.box(part1, "red")
        vis.box(part2, "green")

    if expect:
        for exp, got in zip(expect, (part1.area, part2.area)):
            if exp == got:
                print(got)
            else:
                print(got, "- INCORRECT! expected", exp)
    else:
        print(part1.area)
        print(part2.area)


if __name__ == "__main__":
    solve("input2.txt", expect=(50,24))
    solve("input.txt", "vis.svg")
