N=[[0]+[c>'A'for c in r]for r in open("input.txt")]
W,H=len(N[0]),len(N)+1;N=[[0]*W]+N+[[0]*W];W-=1;S=0
while S!=N:
 S=N;N=[r[:]for r in S]
 for y in range(1,H):
  for x in range(1,W):
   e=S[y-1][x-1:x+2]+S[y][x-1:x+2]+S[y+1][x-1:x+2];c=e.pop(4);n=e.count(2)
   if n<1and c==1:N[y][x]=2
   if n>3and c>1:N[y][x]=1
print sum(r.count(2)for r in S)
