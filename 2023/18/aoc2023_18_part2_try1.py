S,L,U,M=[0,0],[(0,0)],[{0},{0}],[0,0];x=y=0
for l in open("input.txt"):l=l.split()[2];n=int(l[2:7],16);u,v={"0":(1,0),"1":(0,1),"2":(-1,0),"3":(0,-1)}[l[7]];x+=n*u;y+=n*v;L+=[(x,y)];U[0]|={x};U[1]|={y}
for d in(0,1):
 u=sorted(U[d]);n=len(u);M[d]={u[i]:i*2 for i in range(n)};S[d]=[1]
 for i in range(n-1):S[d]+=[u[i+1]-u[i]-1,1]
V=[set(),set(),set()];x,y=M[0][0],M[1][0]
for u,v in L[1:]:
 u,v=M[0][u],M[1][v];d=(u>x)-(u<x);e=(v>y)-(v<y)
 while x-u or y-v:
  x+=d;y+=e
  for f in(-1,0,1):V[f]|={(x-f*e,y+f*d)}
L=V[0]
for f in(1,-1):
 t=e=V[f]-L
 while e and((-1,-1)in e)-1:t|=e;e={(x+u,y+v)for x,y in e for u,v in((0,1),(0,-1),(1,0),(-1,0))}-L-t
 if not e:print(sum(S[0][x]*S[1][y]for x,y in t|L))
