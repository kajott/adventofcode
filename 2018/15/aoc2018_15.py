_,M=enumerate,min
d=map(str.strip,open("input.txt"))
F,U,P,o=[[c=='.'for c in r]for r in d],[],2,0
for y,r in _(d):U+=[[y,x,200,c<'G']for x,c in _(r)if c in"EG"]
N=lambda y,x:[(y+v,x+u)for v,u in((-1,0),(0,-1),(0,1),(1,0))]
E=lambda d,y,x:((d[v][u],v,u)for v,u in N(y,x))
def A(f,y,x):
 d,c,n=[[99]*len(r)for r in f],{(y,x)},set()
 while c or n:
  if not c:c=n;n=set()
  m=99;y,x=c.pop()
  for v,u in N(y,x):
   z=d[v][u];m=M(m,z+1)
   if f[v][u]and z>98:n|={(v,u)}
  d[y][x]=m*(m<99)
 return d
while P<4or o<1:
 P+=1;f,u,r,i,o=[x[:]for x in F],[x[:]for x in U],0,0,1
 while len({z[3]for z in u})>1:
  y,x,h,s=u[i];d=A(f,y,x);t=[]
  for z in u:
   if z[3]-s:t+=E(d,*z[:2])
  h,a,b=M(t)if t else(99,0,0)
  if 0<h<99:h,a,b=M(E(A(f,a,b),y,x));f[y][x]=1;y,x=a,b;u[i][:2]=[y,x];f[y][x]=0
  n=set(N(y,x));n=[(z[2],z[0],z[1],z[3],j)for j,z in _(u)if s-z[3]and tuple(z[:2])in n]
  if n:
   h,a,b,e,j=M(n);h-=(3,P)[s];u[j][2]=h
   if h<=0:
    if e and P>3:o=0;break
    f[a][b]=1;del u[j]
    if j<i:i-=1
  i+=1
  if i>=len(u):r+=1;i=0;u.sort()
 if o:print r*sum(z[2]for z in u)
