import sys,re
p=[map(int,re.findall('-?\d+',x))for x in sys.stdin]
r,g=[],0
for t in xrange(1000,100000,100):
 q=[(x,y,u,v)for x,y,u,v in p if max(abs(x+t*u),abs(y+t*v))<100]
 if len(q)>len(r):r,g=q,t
print g,len(r)
def c(t):
 p=[(x+u*t,y+v*t) for x,y,u,v in r]
 x,y=(min(k[i] for k in p) for i in (0,1))
 p=[(a-x,b-y) for a,b in p]
 w,h=(max(k[i] for k in p)+1 for i in (0,1))
 return w*h,t,w,h,p
a,t,w,h,p=min(c(t) for t in xrange(g-1000,g+1000))
print t,w,h
if max(w,h)<100:
 for y in xrange(h):print ''.join(" #"[(x,y) in p] for x in xrange(w))
