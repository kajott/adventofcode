d,a={},set()
for l in open("input.txt"):x,y,n=l.split()[::2];d[(x,y)]=d[(y,x)]=int(n);a|={x,y}
L=lambda p,r:min(d[(p,n)]+L(n,r-{n})for n in r)if r else 0
print min(L(f,a-{f})for f in a)
