# attempt of a solution using octree subdivision
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

class OctreeCell(object):
    def __init__(self, x, y, z, size):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.corners = [
            (x,        y,        z       ),
            (x,        y,        z + size),
            (x,        y + size, z       ),
            (x,        y + size, z + size),
            (x + size, y,        z       ),
            (x + size, y,        z + size),
            (x + size, y + size, z       ),
            (x + size, y + size, z + size),
        ]
        self.near = [inrange(*c) for c in self.corners]
        self.score = sum(self.near)
        self.dist = abs(x + size/2) + abs(y + size/2) + abs(z + size/2)

    def __cmp__(self, other):
        return cmp(self.score, other.score) or cmp(other.dist, self.dist)

    def __str__(self):
        return "%d near <%d, %d, %d, size %d> (dist=%d)" % (self.score/8, self.x, self.y, self.z, self.size, self.dist)

    def subdivide(self):
        if self.size < 2:
            return [OctreeCell(self.x, self.y, self.z, 0)]
        ss = self.size / 2
        assert self.size == ss * 2
        x0, y0, z0 = self.x, self.y, self.z
        x1, y1, z1 = x0 + ss, y0 + ss, z0 + ss
        return [
            OctreeCell(x0, y0, z0, ss),
            OctreeCell(x0, y0, z1, ss),
            OctreeCell(x0, y1, z0, ss),
            OctreeCell(x0, y1, z1, ss),
            OctreeCell(x1, y0, z0, ss),
            OctreeCell(x1, y0, z1, ss),
            OctreeCell(x1, y1, z0, ss),
            OctreeCell(x1, y1, z1, ss),
        ]


print "coordinate ranges:"
for c in xrange(4):
    k = [x[c] for x in pts]
    print "XYZR"[c], min(k), max(k)

coarse_range = 100000000
coarse_steps = 20

coarse_size = coarse_range / coarse_steps
print "configured coarse grid parameters: %d x %d = %d" % (coarse_steps, coarse_size, coarse_range)
for x in (1,2,4,8,16):
    coarse_size |= coarse_size >> x
coarse_size += 1
coarse_range = coarse_size * coarse_steps
print "quantized coarse grid parameters: %d x %d = %d" % (coarse_steps, coarse_size, coarse_range)


cells = []
crange = range(-coarse_range, coarse_range+1, coarse_size)
for x in crange:
    for y in crange:
        for z in crange:
            cells.append(OctreeCell(x,y,z, coarse_size))

keep_best = 200

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
