import collections as K
C,S=K.defaultdict(set),"start"
for l in open("input.txt"):a,b=l.strip().split('-');C[a]|={b}-{S};C[b]|={a}-{S}
V=lambda p,d:"end"==p[-1]or sum(V(p+[t],c)for t,c in((t,d+(t==t.lower())*(t in p))for t in C[p[-1]])if c<2)
print V([S],0)
