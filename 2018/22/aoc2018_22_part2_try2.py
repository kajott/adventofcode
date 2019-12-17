_=range
import re
n,k,l=map(int,re.findall('\d+',open("input.txt").read()))
w=2*k;h=l+w
m=20183;g=[[(x*16807+n)%m for x in _(w+1)]]+[[((y+1)*48271+n)%m]+w*[0]for y in _(h)]
for y in _(h):
 for x in _(w):g[y+1][x+1]=(g[y][x+1]*g[y+1][x]+n)%m
g[l][k]=0;g=[[c%3for c in r]for r in g]
d={};o,q={(0,0,1,0)},set()
while o or q:
 if not o:o,q=q,set()
 u,v,c,t=o.pop();z=(u,v,c)
 if t<d.get(z,2000):
  d[z]=t;q|={(u,v,n,t+7)for n in(0,1,2)if n!=c and n!=g[v][u]}
  for a,b in((-1,0),(0,-1),(1,0),(0,1)):
   x,y=u+a,v+b
   if(0<=x<=w)*(0<=y<=h)and g[y][x]-c:q|={(x,y,c,t+1)}
print min(d[(k,l,1)],d[(k,l,2)]+7)
