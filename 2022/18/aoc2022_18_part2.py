T,X=tuple,(0,1,2)
G={tuple(map(int,l.split(',')))for l in open("input.txt")}
A={0};q={T([-1]*3)}
while q:A|=q;q={z for z in(T(p[i]+d*(a==i)for i in X)for d in(-1,1)for a in X for p in q)if all(-2<c<22for c in z)}-A-G
print sum(T(p[i]+d*(a==i)for i in X)in A for d in(-1,1)for a in X for p in G)
