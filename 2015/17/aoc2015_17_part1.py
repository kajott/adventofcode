C=map(int,open("input.txt"))
l=len(C)
print sum(sum(C[i]*((n>>i)&1)for i in range(l))==150for n in range(1<<l))
