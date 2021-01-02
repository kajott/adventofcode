M=[0,1+1j,4+1j,5,6,7+1j,10+1j,11,12,13+1j,16+1j,17,18,18-1j,19]
T,E,R={},{},range
for t in open("input.txt").read().strip().split("\n\n"):t=t.split('\n');i=int(t[0][5:-1]);t=[[c<'.'for c in r]for r in t[1:]];v=[t]+[[[r[x]for r in t]for x in R(10)]];v+=[t[::-1]for t in v];v+=[[r[::-1]for r in t]for t in v];T[i]=v;E[i]=[[t[0],t[-1],[r[0]for r in t],[r[-1]for r in t]]for t in v]
P,A,S={},{0},set()
def F(p,t,v,e):
 for q in set(E)-A:[Z(p,q,j)for j in R(8)if E[q][j][e^1]==E[t][v][e]]
def Z(p,t,v):
 if not t in A:A.add(t);P[p]=(t,v);F(p-8,t,v,0);F(p+8,t,v,1);F(p-8j,t,v,2);F(p+8j,t,v,3)
Z(0,min(T),0)
for p in P:
 t,v=P[p];t=T[t][v]
 for y in R(8):S|={p+1j*y+x for x in R(8)if t[x+1][y+1]}
S=[S]+[{p.conjugate()for p in S}];S+=[{p*1j for p in s}for s in S];S+=[{-p for p in s}for s in S]
for s in S:
 a=set()
 for p in s:
  m={p+x for x in M}
  if m<=s:a|=m
 if a:print len(s-a)
