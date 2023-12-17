import heapq as Q
M,E={},enumerate
for Y,r in E(open("input.txt")):
 for X,c in E(r.strip()):M[(X,Y)]=int(c)
q=[(0,0,0,x,1-x,0)for x in(0,1)];p={0}
def G(u,v,m):Q.heappush(q,(c+M.get((x+u,y+v),1E9),x+u,y+v,u,v,m))
while q:
 k=Q.heappop(q);c,x,y,u,v,m=k
 if(k[1:]in p)-1:
  p|={k[1:]};G(-v,u,1);G(v,-u,1)
  if m<3:G(u,v,m+1)
 if x+y==X+Y:q=0
print(c)
