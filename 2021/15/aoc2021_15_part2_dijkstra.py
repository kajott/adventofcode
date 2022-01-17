from heapq import*
M=[map(int,l.strip())for l in open("input.txt")]
u,v=len(M[0]),len(M);w,h=u*5,v*5
M=[[(M[y%v][x%u]+y/v+x/u-1)%9+1for x in range(w)]for y in range(h)]
S=[w*[1e9]for r in M];S[0][0],q,d=0,[(0,0,0)],{0}
while q:
 s,u,v=heappop(q);p={(u,v)}
 if p-d:
  d|=p
  for x,y in((u-1,v),(u+1,v),(u,v-1),(u,v+1)):
   if(0<=x<w)*(0<=y<h):
    n=s+M[y][x]
    if n<S[y][x]:S[y][x]=n;heappush(q,(n,x,y))
print S[-1][-1]
