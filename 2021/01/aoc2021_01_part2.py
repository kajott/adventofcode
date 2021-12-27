N=map(int,open("input.txt"))
print sum(b+c+d>a+b+c for a,b,c,d in zip(N,N[1:],N[2:],N[3:]))
