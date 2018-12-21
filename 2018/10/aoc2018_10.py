_=xrange
import sys,re
r=[map(int,re.findall('-?\d+',x))for x in open("input.txt")]
def c(t):
 p=[(x+u*t,y+v*t)for x,y,u,v in r]
 x,y=(min(k[i]for k in p)for i in(0,1))
 p=[(a-x,b-y)for a,b in p]
 w,h=(max(k[i]for k in p)+1for i in(0,1))
 return w*h,t,w,h,p
a,t,w,h,p=min(c(t)for t in _(9900,10100))
for y in _(h):print''.join(" #"[(x,y)in p]for x in _(w))
print t
