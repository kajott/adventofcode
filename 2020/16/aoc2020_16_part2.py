import re;F=re.findall
I=open("input.txt").read()
R={m[0]:map(int,m[1:])for m in F('(.*): (\d+)-(\d+) or (\d+)-(\d+)',I)}
T=[map(int,t.split(','))for t in F('\d+,[0-9,]+',I)]
A=len(R)
P={c:set(range(A))for c in R}
F=[0]*A
def C(r,n):a,b,c,d=R[r];return(a<=n<=b)+(c<=n<=d)
for t in T:
 if any(any(C(r,n)for r in R)<1for n in t)<1:
  for r in R:P[r]-={i for i in P[r]if C(r,t[i])<1}
z=1
while all(F)<1:
 x={-1}
 for r in R:
  if len(P[r])==1:
   i=P[r].pop();F[i]=r;x|={i}
   if r[:2]=="de":z*=T[0][i]
 for r in R:P[r]-=x
print z
