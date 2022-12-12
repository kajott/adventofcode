N,G=enumerate,{}
for y,r in N(open("input.txt")):
 for x,c in N(r):
  p=x+y*1j;z=ord(c)
  if z==83:S=p;z=97
  if z==69:E=p;z=122
  G[p]=z
P={E:0};q={E}
while q:
 p=q.pop();d=P[p]+1
 for n in(p+1,p-1,p+1j,p-1j):
  if G.get(n)>G[p]-2and P.get(n,1E6)>d:P[n]=d;q|={n}
print P[S]
print min(P[p]for p in P if G[p]<98)
