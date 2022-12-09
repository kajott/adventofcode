E,F=enumerate,{}
for y,r in E(open("input.txt")):
 for x,z in E(r.strip()):F[x+1j*y]=int(z)+2
def S(p,d):
 z=F[p];n=t=1
 while(t<z)*t:p+=d;t=F.get(p,0);n+=t>0
 return n-1
print max(S(p,1)*S(p,-1)*S(p,1j)*S(p,-1j)for p in F)
