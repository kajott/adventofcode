_=abs
import re,itertools as I
b=[map(int,re.findall('-?\d+',x))for x in open("input.txt")]
S=lambda x,y,z:(sum(_(x-u)+_(y-v)+_(z-w)<=r for u,v,w,r in b),-_(x)-_(y)-_(z),x,y,z)
p=S(*(sum(p[c]for p in b)/len(b)for c in(0,1,2)))
r=1<<20;n=(-1,0,1)
while r:
 m=max(S(p[2]+r*x,p[3]+r*y,p[4]+r*z)for x,y,z in I.product(n,n,n))
 if m>p:p=m
 else:r/=2
print-p[1]
