E=enumerate
R=list(open("input.txt"))
v,P,T={0},{},{}
for y,r in E(R):
 for x,c in E(r):
  p=x+y*1j
  if'.'==c:
   for i,j,k,l in((-2,0,-1,0),(1,0,2,0),(0,-2,0,-1),(0,1,0,2)):
    z=R[y+i][x+j]+R[y+k][x+l]
    if z.isalpha():P[z]=P.get(z,[])+[p]
  else:v|={p}
n={P.pop('AA')[0]}
m={P.pop('ZZ')[0]}
for a,b in P.values():T[a]=b;T[b]=a
d=0
while not n&m:
 c=n;n=set();v|=c;d+=1
 for p in c:n|={p-1,p+1,p-1j,p+1j,T.get(p,0)}-v
print d
