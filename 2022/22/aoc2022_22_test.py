#!/usr/bin/env python3
"""scratchpad for my AoC 2022/22 solution"""
import re

infile, facesize = "input.txt",50
#infile, facesize = "input2.txt",4

def D():
    xmax = max(x for x,y in M)+1
    ymax = max(y for x,y in M)+1
    for y in range(1,ymax):
        print(''.join(".# X@!"[M.get((x,y),2)+(x==px and y==py)*3]for x in range(1,xmax)))

M={}
I=[]
P={}
y=0
for line in open(infile):
    if 'L' in line:
        I=re.findall('\d+|R|L',line)
    else:
        y+=1
        for x, c in enumerate(line):
            if c=='#':M[(x+1,y)]=1
            if c=='.':M[(x+1,y)]=0
#print(I)

def move(px,py,dx,dy):
    npx,npy = px+dx,py+dy
    ndx,ndy = dx,dy
    if not (npx,npy) in M:
        if P: npx,npy,ndx,ndy = P[(npx,npy, ndx,ndy)]
        elif dx>0:npx=min(x for x,y in M if y==npy)
        elif dx<0:npx=max(x for x,y in M if y==npy)
        elif dy>0:npy=min(y for x,y in M if x==npx)
        elif dy<0:npy=max(y for x,y in M if x==npx)
    assert(npx,npy)in M
    if M[(npx,npy)]: return (px,py, dx,dy, True)
    else: return (npx,npy, ndx,ndy, False)

ipx,ipy,*dummy = move(9999,1,1,0)

def run():
    global px,py
    px,py,dx,dy = ipx,ipy, 1,0
    for ins in I:
        if ins.isdigit():
            for s in range(int(ins)):
                px,py,dx,dy,wall = move(px,py,dx,dy)
                if wall: break
        elif ins == 'R': dx,dy=(-dy,dx)
        elif ins == 'L': dx,dy=(dy,-dx)
    f = [(1,0), (0,1), (-1,0), (0,-1)].index((dx,dy))
    print(px,py, dx,dy, f, "=>", 1000*py + 4*px + f)
run()

class Walker:
    def __init__(self, px,py, dx,dy, lookdir):
        self.lookdir = lookdir
        self.px, self.py = px, py
        self.setdir(dx,dy)
    def setdir(self, dx,dy):
        self.dx, self.dy = dx, dy
        self.sx = -self.lookdir * dy
        self.sy =  self.lookdir * dx
        assert not (self.px+self.dx, self.py+self.dy) in M
        assert     (self.px+self.sx, self.py+self.sy) in M
    def make_portal(self, other):
        P[(self.px,self.py, -self.sx,-self.sy)] = (other.px+other.sx,other.py+other.sy, other.sx,other.sy)
    def walk_and_check(self):
        # returns tuple (can_continue, corner_found)
        self.px += self.dx
        self.py += self.dy
        if (self.px,self.py) in M: return (False, False)  # ran into another side (is that even possible?)
        if (self.px+self.sx, self.py+self.sy) in M: return (True, False)  # can continue along same edge
        # else: turn around the corner
        self.px += self.sx
        self.py += self.sy
        self.setdir(self.sx, self.sy)
        return (True, True)
    def __str__(self):
        return f"Walker({self.px:3d},{self.py:3d}; {self.lookdir:+d}; {self.dx:+d},{self.dy:+d}; {self.sx:+d},{self.sy:+d})"
def walk(px,py, ldx,ldy, rdx,rdy):
    l = Walker(px,py, ldx,ldy, -1)
    r = Walker(px,py, rdx,rdy, +1)
    print("  ", l, r)
    while True:
        l.make_portal(r)
        r.make_portal(l)
        lcont, lcorn = l.walk_and_check()
        rcont, rcorn = r.walk_and_check()
        if not(lcont) or not(rcont) or (lcorn and rcorn): break
for cx in range(facesize, facesize*10, facesize):
    for cy in range(facesize, facesize*10, facesize):
        corner = 8 * ((cx,  cy)   in M) \
               + 4 * ((cx+1,cy)   in M) \
               + 2 * ((cx,  cy+1) in M) \
               + 1 * ((cx+1,cy+1) in M)
        if corner == 0b0111: print(f"_| corner at {cx},  {cy}");   walk(cx,  cy,   -1,0, 0,-1)
        if corner == 0b1011: print(f"|_ corner at {cx+1},{cy}");   walk(cx+1,cy,   0,-1, +1,0)
        if corner == 0b1101: print(f"~| corner at {cx},  {cy+1}"); walk(cx,  cy+1, 0,+1, -1,0)
        if corner == 0b1110: print(f"|~ corner at {cx+1},{cy+1}"); walk(cx+1,cy+1, +1,0, 0,+1)
print(len(P) / facesize, "sides")
D()
run()
