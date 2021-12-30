E,M,Q=enumerate,{},lambda q:M.get(q,9)
for y,l in E(open("input.txt")):
 for x,i in E(l.strip()):M[x+1j*y]=int(i)
def A(p):
 v,q={p},{p}
 while q:
  v|=q;q=set()
  for p in v:q|={x for x in(p+1,p-1,p+1j,p-1j)if Q(x)<9}-v
 return len(v)
b=sorted(A(p)for p in M if M[p]<min(Q(p+1),Q(p-1),Q(p-1j),Q(p+1j)))
print b[-3]*b[-2]*b[-1]
