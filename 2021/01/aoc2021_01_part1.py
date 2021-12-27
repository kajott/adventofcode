N=map(int,open("input.txt"))
print sum(a>b for a,b in zip(N[1:],N))
