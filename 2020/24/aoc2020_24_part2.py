import re
D,F={'e':2,'w':-2,'se':1+1j,'sw':1j-1,'ne':1-1j,'nw':-1-1j,'x':0},{}
for l in open("input.txt"):p=sum(D[x]for x in re.findall('|'.join(D),l));F[p]=1-F.get(p,0)
N=lambda p:{p+d for d in D.values()}
for t in range(100):
 F,I,a={},F,{0}
 for p in I:a|=N(p)
 for p in a:
  c=I.get(p,0);n=sum(I.get(d,0)for d in N(p))
  if(n<2or n>3)*c:c=0
  if(c<1)*(n==2):c=1
  if c:F[p]=1
print sum(F.values())
