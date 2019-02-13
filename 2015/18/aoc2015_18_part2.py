_=range
g=[[c<'.'for c in r.strip()]+[0]for r in open("input.txt")]
w,h=len(g[0]),len(g)
g+=[[0]*w]
def F():g[0][0]=g[0][w-2]=g[h-1][0]=g[h-1][w-2]=1
for t in _(100):
 F();o=g;g=[[0]*w for y in _(h+1)]
 for y in _(h):
  for x in _(w-1):c=o[y][x];n=sum(o[v][x-1]+o[v][x]+o[v][x+1]for v in(y-1,y,y+1))-c;g[y][x]=(n<4)*(n>2-c)
F();print sum(map(sum,g))
