#!/usr/bin/env python2
"""
scribble to determine the static portals and various encodings for it,
based on the parser and portal generator from aoc2022_22_part2_try1.py
"""

import re
E,M,P=enumerate,[],{}
for y,I in E(open("input.txt")):M+=[(y+1,x+1,c)for x,c in E(I)if' '<c]
p,f=M[0][0]*1j+M[0][1],0
M={y*1j+x:c>'#'for y,x,c in M}
C=lambda z:z in M
for s in M:
 for a in(0,1,2,3):
  b=a+1&3;u,v=1j**a,1j**b;l,r=s+u,s+v;c=2-C(s+u)*C(s+v)*(1-C(s+u+v))
  while c<2:
   P[(l,a+1&3)]=(r,b+1&3);P[(r,b-1&3)]=(l,a-1&3);l+=u;r+=v;c=0
   if C(l+1j**(a+1))+C(r+1j**(b-1)):c=2
   if C(l)-1:l-=u;a=a-1&3;u=1j**a;c+=1
   if C(r)-1:r-=v;b=b+1&3;v=1j**b;c+=1

def facing(delta): return [1,1j,-1,-1j].index(delta)

oldP = dict(P.iteritems())
assert P == oldP
pmap = []
while P:
    astart, aface = min(P, key=lambda k:(k[0].imag, k[0].real, k[1]))
    bstart, bface = P[(astart, aface)]
    bface = bface+2&3
    adirs = [d for d in (1,-1,1j,-1j) if (astart + d, aface) in P]
    assert len(adirs) == 1
    adir = adirs.pop()
    bdir = P[(astart + adir, aface)][0] - bstart
    print astart, adir, facing(adir), aface, "<->", bstart, bdir, facing(bdir), bface
    pmap.append(((astart, adir, aface), (bstart, bdir, bface)))
    for n in range(50):
        assert P[(astart, aface)] == (bstart, bface+2&3)
        assert P[(bstart, bface)] == (astart, aface+2&3)
        del P[(astart, aface)]
        del P[(bstart, bface)]
        astart += adir
        bstart += bdir

print "pure pmap:", repr(tuple(pmap)).replace(' ', '')
P={}
for p in pmap:
    for d in (0,1):
        for n in range(50):
            P[(p[d][0]+p[d][1]*n, p[d][2])] = (p[1-d][0]+p[1-d][1]*n, p[1-d][2]+2&3)
assert P == oldP

sfpmap=[]
for p in pmap:
    sfpmap.append(tuple(list(p[0]) + list(p[1])))
print "semi-flat pmap:", repr(tuple(sfpmap)).replace(' ', '')
P={(p[d]+p[d+1]*n,p[d+2]):(p[3-d]+p[4-d]*n,p[5-d]+2&3)for n in range(50)for d in(0,3)for p in sfpmap}
assert P == oldP

cfpmap=[]
for p in pmap:
    for d in p:
        x = int(d[0].real) - 1
        y = int(d[0].imag) - 1
        xd =      x / 50
        xr = int((x % 50) > 1)
        yd =      y / 50
        yr = int((y % 50) > 1)
        f = facing(d[1])
        assert d[0] == xd*50 + xr*49 + 1 + yd*50j + yr*49j + 1j
        assert d[1] == 1j**f
        cfpmap += [xd, xr, yd, yr, f, d[2]]
print "componentized pmap:", repr(tuple(cfpmap)).replace(' ', '')
n=0
for d in cfpmap[::-1]:
    assert 0 <= d < 4
    n = (n << 2) + d
print "bits:", len(cfpmap) * 2
print "decimal:", n
print "hex:    ", hex(n)
def b36_encode(i):  # https://stackoverflow.com/a/60498038, 'cause I'm lazy
    if i < 0: return "-" + b36_encode(-i)
    if i < 36: return "0123456789abcdefghijklmnopqrstuvwxyz"[i]
    return b36_encode(i // 36) + b36_encode(i % 36)
print "base36: ", "int('" + b36_encode(n) + "',36)"
assert len(cfpmap) == 7 * 2 * 6
C=lambda i:cfpmap[i]
T=lambda b,n,x:(C(b)*50+C(b+1)*49+1+C(b+2)*50j+C(b+3)*49j+1j+n*1j**C(b+4),C(b+5)^x)
P={T(b+d,n,0):T(b+6-d,n,2)for n in range(50)for d in(0,6)for b in range(0,84,12)}
assert P == oldP
