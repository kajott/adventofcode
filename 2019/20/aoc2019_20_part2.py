E=enumerate
R=list(open("input.txt"))
W={0};P={}
for y,r in E(R):
 for x,c in E(r):
  if'.'==c:
   for i,j,k,l in((-2,0,-1,0),(1,0,2,0),(0,-2,0,-1),(0,1,0,2)):
    z=R[y+i][x+j]+R[y+k][x+l]
    if z.isalpha():P[z]=P.get(z,[])+[(1-2*((x<3)+(y<3)+(x>len(r)-5)+(y>len(R)-5)),x,y)]
  else:W|={(x,y)}
n,m=({(x,y,0)}for d,x,y in(P.pop(u)[0]for u in('AA','ZZ')))
T={}
for a,b in map(sorted,P.values()):z,x,y=a;k,i,j=b;T[(x,y)]=(i,j,z);T[(i,j)]=(x,y,k)
d=0;v={0}
while not n&m:
 v|=n;c=n;n=set();d+=1
 for x,y,z in c:
  i,j,k=T.get((x,y),(0,0,-99));k+=z
  if k>=0:n|={(i,j,k)}
  n|={(x,y,z)for x,y,z in((x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z))if{(x,y)}-W}
 n,m=m,n-v
print d
