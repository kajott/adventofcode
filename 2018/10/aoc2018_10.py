import sys,re
r=[map(int,re.findall('-?\d+',x)) for x in sys.stdin]
def c(t):
 p=[(x+u*t,y+v*t) for x,y,u,v in r]
 x,y=(min(k[i] for k in p) for i in (0,1))
 p=[(a-x,b-y) for a,b in p]
 w,h=(max(k[i] for k in p)+1 for i in (0,1))
 return w*h,t,w,h,p
a,t,w,h,p=min(c(t) for t in xrange(9900,10100))
print t
for y in xrange(h):print ''.join(" #"[(x,y) in p] for x in xrange(w))
