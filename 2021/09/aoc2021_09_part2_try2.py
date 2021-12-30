E,M,Q=enumerate,{},lambda q:M.get(q,9)<9
for y,l in E(open("input.txt")):
 for x,i in E(l.strip()):M[x+1j*y]=int(i)
a,b={p for p in M if Q(p)},[]
while a:
 p=a.pop();v,q={p},{p}
 while q:
  v|=q;q=set()
  for p in v:q|={x for x in(p+1,p-1,p+1j,p-1j)if Q(x)}-v
 b+=[len(v)];a-=v
b.sort()
print b[-3]*b[-2]*b[-1]
