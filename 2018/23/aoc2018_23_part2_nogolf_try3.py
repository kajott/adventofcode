# attempt of a solution using random refinement
# (kinda like a genetic algorithm)
# -- works, but takes very long to compute and the most useful part
# of the computation is the refinement at the end

import re
import random
import itertools

pts = [map(int,re.findall('-?\d+',x)) for x in open("input.txt")]

_cache = {}
def inrange(x,y,z):
    try:
        return _cache[(x,y,z)]
    except KeyError:
        d = sum(abs(x-u) + abs(y-v) + abs(z-w) <=r for u,v,w,r in pts)
        _cache[(x,y,z)] = d
        return d

class Point(object):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.score = inrange(x,y,z)
        self.dist = abs(x) + abs(y) + abs(z)

    def __cmp__(self, other):
        return cmp(self.score, other.score) or cmp(other.dist, self.dist)

    def __str__(self):
        return "%d near <%d, %d, %d> dist %d" % (self.score, self.x, self.y, self.z, self.dist)

    def getrandom(self, count=1, radius=1):
        # bias the range a bit towards the coordinate origin
        x0 = self.x - radius
        y0 = self.y - radius
        z0 = self.z - radius
        radj = radius / 2
        x0 += radj if x0 < 0 else -radj
        y0 += radj if y0 < 0 else -radj
        z0 += radj if z0 < 0 else -radj
        r1 = 2 * radius + 1
        return [Point(
            random.randrange(x0, x0 + r1),
            random.randrange(y0, y0 + r1),
            random.randrange(z0, z0 + r1)
        ) for x in xrange(count)]

keep_best, add_new = 10, 10

cells = [Point(*p[:3]) for p in pts]
radius = min(p[-1] for p in pts)
while radius:
    cells.sort(reverse=True)
    del cells[keep_best:]
    print "(r=%d)" % radius, cells[0]
    newcells = []
    for c in cells:
        newcells += [c] + c.getrandom(add_new, radius)
    cells = newcells
    radius = radius * 3 / 4
c = max(cells)

print "(end)", c

radius = 1<<20
while radius:
    for dx,dy,dz in itertools.product((-1,0,1), (-1,0,1), (-1,0,1)):
        p = Point(c.x+dx*radius, c.y+dy*radius, c.z+dz*radius)
        if p > c:
            c = p
            print "(r=%d)" % radius, c
            break
    else:
        radius /= 2
