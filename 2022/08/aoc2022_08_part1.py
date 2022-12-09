E,F=enumerate,{}
for y,r in E(open("input.txt")):
 for x,z in E(r.strip()):F[x+1j*y]=int(z)+1
def V(p,d):
 z=F[p];t=0
 while t<z:
  p+=d;t=F.get(p)
  if t<1:return 1
print sum(any(V(p,d)for d in(1,-1,1j,-1j))for p in F)
