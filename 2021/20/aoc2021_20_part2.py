_,T=range,50
f=open("input.txt");L=f.readline
B=lambda l:[c=='#'for c in l]
R=B(L());L()
p=T*2*[0];M=[p+B(l)+p for l in f];w=len(M[0])
p=T*2*[w*[0]];M=p+M+p;h=_(1,len(M)-1);w=_(1,w-1)
for t in _(T):
 P=M;M=[r[:]for r in P]
 for y in h:
  for x in w:
   k=0
   for v in _(y-1,y+2):
    for u in _(x-1,x+2):k=2*k+P[v][u]
   M[y][x]=R[k]
print sum(sum(r[T:-T])for r in M[T:-T])
