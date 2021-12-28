P=map(int,open("input.txt").read().split(','))
print min(sum(abs(p-t)for p in P)for t in range(max(P)))
