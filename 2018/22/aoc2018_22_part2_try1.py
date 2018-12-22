_=range
import re,collections as C
n,k,l=map(int,re.findall('\d+',open("input.txt").read()))
w=2*k;h=l+w
m=20183;g=[[(x*16807+n)%m for x in _(w+1)]]+[[((y+1)*48271+n)%m]+w*[0]for y in _(h)]
for y in _(h):
 for x in _(w):g[y+1][x+1]=(g[y][x+1]*g[y+1][x]+n)%m
g[l][k]=0;g=[[c%3for c in r]for r in g]
d=C.defaultdict(lambda:2000);o=(0,0,1);d[o]=0;o,q={o},set()
while o or q:
 if not o:o,q=q,set()
 i=o.pop();u,v,c=i;i=d[i]
 for a,b in((-1,0),(0,-1),(1,0),(0,1)):
  x,y=u+a,v+b
  if(0<=x<=w)*(0<=y<=h):
   for n in(0,1,2):
    if n!=g[y][x]and n!=g[v][u]:
     z=(x,y,n);t=i+1+7*(n!=c)
     if t<d[z]:d[z]=t;q|={z}
print min(d[(k,l,1)],d[(k,l,2)]+7)
