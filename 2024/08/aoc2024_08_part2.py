E,F=enumerate,{}
for H,l in E(open("input.txt")):
 for W,c in E(l.strip()):F[c]=F.get(c,[])+[W+H*1j]
del F['.']
print(sum((0<=p.real<=W)*(0<=p.imag<=H)for p in{a+n*(b-a)for n in range(-W,W)for p in F.values()for a in p for b in p}))
