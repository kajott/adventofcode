import re
P=[map(int,re.findall('-?\d+',l))for l in open("input.txt")]
I=range(len(P));C=(0,1,2);V=[[0,0,0]for p in I]
S=lambda a,b:(a<b)-(a>b)
for t in range(1000):
 for a in I:
  for b in I:
   for c in C:V[a][c]+=S(P[a][c],P[b][c])
 for a in I:
  for c in C:P[a][c]+=V[a][c]
E=lambda x:sum(map(abs,x))
print sum(E(p)*E(v)for p,v in zip(P,V))
