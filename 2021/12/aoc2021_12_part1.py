import collections as K
C=K.defaultdict(set)
for l in open("input.txt"):a,b=l.strip().split('-');C[a]|={b};C[b]|={a}
V=lambda p:"end"==p[-1]or sum(V(p+[t])for t in C[p[-1]]if t!=t.lower()or(t in p)-1)
print V(["start"])
