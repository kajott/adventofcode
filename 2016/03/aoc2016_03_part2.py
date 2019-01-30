x=map(int,open("input.txt").read().split())
x=x[::3]+x[1::3]+x[2::3]
print sum(a+b>c for a,b,c in(sorted(x[i:i+3])for i in range(0,len(x),3)))
