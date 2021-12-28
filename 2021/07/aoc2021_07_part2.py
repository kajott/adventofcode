P=map(int,open("input.txt").read().split(','))
f=lambda x:x*(x+1)/2
print min(sum(f(abs(p-t))for p in P)for t in range(max(P)))
