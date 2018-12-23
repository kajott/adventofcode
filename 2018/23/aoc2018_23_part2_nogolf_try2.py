# attempt of a solution using octahedron endpoint refinement
# DOES NOT WORK!

import re

pts = [map(int,re.findall('-?\d+',x)) for x in open("input.txt")]

_cache = {}
def inrange(x,y,z):
    try:
        return _cache[(x,y,z)]
    except KeyError:
        d = sum(abs(x-u) + abs(y-v) + abs(z-w) <=r for u,v,w,r in pts)
        _cache[(x,y,z)] = d
        return d

class Octahedron(object):
    def __init__(self, x,y,z, size):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.score = inrange(x,y,z)
        self.dist = abs(x) + abs(y) + abs(z)

    def __cmp__(self, other):
        return cmp(self.score, other.score) or cmp(other.dist, self.dist)

    def __str__(self):
        return "%d near <%d, %d, %d, size %d> (dist=%d)" % (self.score, self.x, self.y, self.z, self.size, self.dist)

    def subdivide(self):
        if self.size < 1:
            return [self]
        ss = self.size / 2
        return [
            Octahedron(self.x, self.y, self.z, ss),
            Octahedron(self.x + self.size, self.y, self.z, ss),
            Octahedron(self.x - self.size, self.y, self.z, ss),
            Octahedron(self.x, self.y + self.size, self.z, ss),
            Octahedron(self.x, self.y - self.size, self.z, ss),
            Octahedron(self.x, self.y, self.z + self.size, ss),
            Octahedron(self.x, self.y, self.z - self.size, ss),
        ]

cells = [Octahedron(*p) for p in pts]

keep_best = 100

print "starting subdivisions with keep_best=%d ..." % keep_best

while any(c.size for c in cells):
    cells.sort(reverse=True)
    del cells[keep_best:]
    print cells[0]
    newcells = []
    for c in cells:
        newcells += c.subdivide()
    cells = newcells

print max(cells)
