import re
F,C,G,V=frozenset,{},{},{}
for l in open("input.txt"):m=re.findall('[A-Z]{2}|\d+',l);r=int(m.pop(1));V[m[0]]=(r,m[1:])
for s in V:
 G[s]={s:0};q={s}
 while q:
  p=q.pop();d=G[s][p]+1
  for n in V[p][1]:
   if d<G[s].get(n,99):G[s][n]=d;q|={n}
def D(C,N,*s):
 p,t,v=s
 if t<1or not(v and C):return 0
 if s in C:return C[s]
 r=D(N,0,'AA',26,v)
 for q in v:
  k=t-1-G[p][q]
  if k>0:r=max(r,k*V[q][0]+D(C,N,q,k,F(set(v)-{q})))
 C[s]=r;return r
print D({0:0},{0:0},'AA',26,F(p for p in V if V[p][0]))
