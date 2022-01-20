_=range
f=open("input.txt");L=f.readline
B=lambda l:[c=='#'for c in l]
R=B(L());L()
p=[0]*4;M=[p+B(l)+p for l in f];w=len(M[0])
p=[w*[0]]*4;M=p+M+p;h=_(1,len(M)-1);w=_(1,w-1)
for t in"12":
 P=M;M=[r[:]for r in P]
 for y in h:
  for x in w:
   k=0
   for v in _(y-1,y+2):
    for u in _(x-1,x+2):k=2*k+P[v][u]
   M[y][x]=R[k]
print sum(sum(r[2:-2])for r in M[2:-2])
