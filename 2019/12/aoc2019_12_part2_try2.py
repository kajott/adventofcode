import re,fractions as F
P=[map(int,re.findall('-?\d+',l))for l in open("input.txt")]
N=len(P);I=range(N)
S=lambda a,b:(a<b)-(a>b)
def Z(s):
 s=list(s)+N*[0];k,t={0},0
 while 1:
  z=tuple(s)
  if z in k:return t
  k|={z};t+=1
  for a in I:s[a+N]+=sum(S(s[a],s[b])for b in I)
  for a in I:s[a]+=s[a+N]
L=lambda a,b:a*b/F.gcd(a,b)
a,b,c=map(Z,zip(*P))
print L(a,L(b,c))
