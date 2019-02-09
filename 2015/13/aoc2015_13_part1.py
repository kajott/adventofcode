import collections as C,itertools as I
d,a=C.defaultdict(dict),set()
for l in open("input.txt"):w=l.split();x,y=w[0][0],w[-1][0];d[x][y]=int(w[3])*(2*(w[2]<'l')-1);a|={x,y}
n=len(a)
S=lambda x:sum(d[x[i]][x[i-1]]+d[x[i]][x[(i+1)%n]]for i in range(n))
print max(map(S,I.permutations(a)))
