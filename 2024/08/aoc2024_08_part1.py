E,F,A=enumerate,{},set()
for H,l in E(open("input.txt")):
 for W,c in E(l.strip()):F[c]=F.get(c,[])+[W+H*1j]
del F['.']
for p in F.values():
 for i,a in E(p):
  for b in p[i+1:]:A|={2*a-b,2*b-a}
print(sum((0<=p.real<=W)*(0<=p.imag<=H)for p in A))
