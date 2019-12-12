import re,fractions as F
P=[map(int,re.findall('-?\d+',l))+[0,0,0]for l in open("input.txt")]
I=range(len(P));C=(0,1,2)
S=lambda a,b:(a<b)-(a>b)
k,r,t=[{0},{0},{0}],[0,0,0],0
while not min(r):
 s=[]
 for p in P:s+=p
 for c in C:
  z=tuple(s[c::3])
  if r[c]<1and z in k[c]:r[c]=t
  else:k[c]|={z}
 t+=1
 for a in I:
  for c in C:P[a][c+3]+=sum(S(P[a][c],P[b][c])for b in I)
 for a in I:
  for c in C:P[a][c]+=P[a][c+3]
L=lambda a,b:a*b/F.gcd(a,b)
a,b,c=r;print L(a,L(b,c))
