_=sorted
V=lambda p:all(w!=p[i-1]for i,w in enumerate(p))
print sum(V(_(_(w)for w in p.strip().split()))for p in open("input.txt"))
