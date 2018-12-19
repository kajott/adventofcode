d=map(str.strip,open("input.txt"))
F,U,P,o=[[c=='.'for c in r]for r in d],[],2,0
for y,r in enumerate(d):
 for x,c in enumerate(r):
  if c in"EG":U.append([y,x,200,c=='E'])
def N(y,x):
 for v,u in((-1,0),(0,-1),(0,1),(1,0)):yield(y+v,x+u)
E=lambda d,y,x:((d[v][u],v,u)for v,u in N(y,x))
def A(f,y,x):
 d,c,n=[[99]*len(r)for r in f],set([(y,x)]),set()
 while c or n:
  if not c:c=n;n=set()
  m=99;y,x=c.pop()
  for v,u in N(y,x):
   z=d[v][u];m=min(m,z+1)
   if f[v][u] and z==99:n.add((v,u))
  d[y][x]=m*(m<99)
 return d
while P<4or o==0:
 P+=1;f,u,r,i,o=[x[:]for x in F],[x[:]for x in U],0,0,1
 while len(set(z[3]for z in u))>1:
  y,x,h,s=u[i];d=A(f,y,x);t=[]
  for z in u:
   if z[3]!=s:t.extend(E(d,*z[:2]))
  h,a,b=min(t)if t else(99,0,0)
  if 0<h<99:h,a,b=min(E(A(f,a,b),y,x));f[y][x]=1;y,x=a,b;u[i][:2]=[y,x];f[y][x]=0
  n=set(N(y,x));n=[(z[2],z[0],z[1],z[3],j)for j,z in enumerate(u)if z[3]!=s and tuple(z[:2])in n]
  if n:
   h,a,b,e,j=min(n);h-=(3,P)[s];u[j][2]=h
   if h<=0:
    if e and P>3:o=0;break
    f[a][b]=1;del u[j]
    if j<i:i-=1
  i+=1
  if i>=len(u):r+=1;i=0;u.sort()
 if o:print r*sum(z[2]for z in u)
