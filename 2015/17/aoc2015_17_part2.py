C=map(int,open("input.txt"))
l=len(C);r=range(l)
b=[sum((n>>i)&1for i in r)for n in range(1<<l)if sum(C[i]*((n>>i)&1)for i in r)==150]
print sum(x==min(b)for x in b)
