#!/usr/bin/env python3
import re

Boundary = 4000000

class Scanner:
    def __init__(self, line):
        self.x, self.y, self.bx, self.by = map(int, re.findall(r'-?\d+', line))
        self.d = abs(self.x - self.bx) + abs(self.y - self.by)
        self.marked = False
        self.color = "black"

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

class SVGGenerator:
    margin = 100000
    scale = 2.0 / 10000
    dotradius = 4

    def __init__(self, filename, x0, y0, x1, y1):
        x0 -= self.margin
        y0 -= self.margin
        x1 += self.margin
        y1 += self.margin
        self.x0 = x0
        self.y0 = y0
        self.f = open(filename, 'w')
        self.f.write('<?xml version="1.0" encoding="utf-8" standalone="yes" ?>')
        self.f.write(f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{int((x1-x0)*self.scale+0.9)}" height="{int((y1-y0)*self.scale+0.9)}">\n')
        x0, y0 = self.cotrans(0, 0)
        x1, y1 = self.cotrans(Boundary, Boundary)
        self.f.write(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="none" stroke="black" stroke-width="1px" />\n')

    def cotrans(self, x,y):
        return ((x - self.x0) * self.scale, (y - self.y0) * self.scale)

    def diamond(self, x, y, d, color="black", contour=False):
        x, y = self.cotrans(x, y)
        d *= self.scale
        path = f"M {x} {y-d} l {d} {d} l {-d} {d} l {-d} {-d} z"
        if contour:
            self.f.write(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="1" />\n')
        else:
            self.f.write(f'<path d="{path}" fill="{color}" stroke="none" opacity="0.1" />\n')

    def dot(self, x,y, color="black", marked=False, small=False, scale=1):
        r = self.dotradius * scale
        if small: r /= 2
        x, y = self.cotrans(x, y)
        if small:
            self.f.write(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r}" fill="black" stroke="{color}" stroke-width="0.5" />\n')
        else:
            self.f.write(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r}" fill="{color}" stroke="none" />\n')
            if marked:
                self.f.write(f'<ellipse cx="{x}" cy="{y}" rx="{r+1.5*scale}" ry="{r+1.5*scale}" fill="none" stroke="{color}" stroke-width="{scale}" />\n')

    def close(self):
        self.f.write('</svg>\n')
        self.f.close()

def brev(l):
    if len(l) < 2: return l
    return brev(l[0::2]) + brev(l[1::2])

if __name__ == "__main__":
    with open("input.txt") as f:
        scanners = list(map(Scanner, f))

    # mark the four relevant scanners
    for a in scanners:
        for b in scanners:
            if a.dist(b) == (a.d + b.d + 2):
                a.marked = True

    # sort and shuffle to improve color variation
    scanners = brev(sorted(scanners, key=lambda s: s.x + s.y))

    # assign HSL colors
    def hsl(h):
        h = abs(768 - (h % 1536)) - 256
        return max(0, min(255, h))
    h, l = 0, 1
    for s in scanners:
        r = hsl(h)
        g = hsl(h + 512)
        b = hsl(h + 1024)
        r -= r >> l
        g -= g >> l
        b -= b >> l
        s.color = f"#{r:02X}{g:02X}{b:02X}"
        l = 4 - l
        h += 1536 // len(scanners)

    # get bounding box
    xx = [s.x for s in scanners] + [s.bx for s in scanners] + [0, Boundary]
    yy = [s.y for s in scanners] + [s.by for s in scanners] + [0, Boundary]

    # generate SVG
    svg = SVGGenerator("aoc2022_15_vis.svg", min(xx), min(yy), max(xx), max(yy))
    for s in scanners:  # shapes
        svg.diamond(s.x, s.y, s.d, s.color, False)
    for s in scanners:  # outlines and dots
        svg.diamond(s.x, s.y, s.d, s.color, True)
        svg.dot(s.x, s.y, s.color, marked=s.marked)
        svg.dot(s.bx, s.by, s.color, small=True)

    # solve part 2
    nc = sum(s.marked for s in scanners)
    cx = sum(s.x / nc for s in scanners if s.marked)
    cy = sum(s.y / nc for s in scanners if s.marked)
    bset = set()
    for s in scanners:
        if not s.marked: continue
        dx = 1 - 2 * (s.x > cx)
        dy = 1 - 2 * (s.y > cy)
        d = s.d + 1
        line = {(s.x + dx * (d - i), s.y + dy * i) for i in range(d)}
        if bset: bset &= line
        else:    bset  = line
    assert len(bset) == 1

    # write final point and be done
    svg.dot(*bset.pop(), color="red", scale=1.5, marked=True)
    svg.close()
