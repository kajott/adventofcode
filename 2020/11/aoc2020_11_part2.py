_=enumerate
S,N=0,{}
for y,r in _(open("input.txt")):
 for x,c in _(r):
  if'A'<c:N[y*1j+x]=0
def L(p,d):
 while 1:
  p+=d;u,v=p.real,p.imag
  if p in S:return S[p]
  if max(u,v)>99or min(u,v)<0:return 0
while S!=N:
 S,N=N,{}
 for p,c in S.items():
  n=sum(L(p,d)for d in(-1-1j,-1j,1-1j,-1,1,1j-1,1j,1+1j))
  if n+c<1:c=1
  elif n>4and c:c=0
  N[p]=c
print sum(S.values())
