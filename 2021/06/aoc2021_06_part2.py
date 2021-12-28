F=map(int,open("input.txt").read().split(','))
F=[F.count(x)for x in range(9)]
for d in range(256):F=F[1:]+F[:1];F[6]+=F[-1]
print sum(F)
