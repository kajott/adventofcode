d=map(int,open("input.txt").read().strip())
print sum(x for i,x in enumerate(d)if x==d[i-len(d)/2])
