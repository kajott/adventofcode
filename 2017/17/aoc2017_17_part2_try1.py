N=345
class X:pass
p=z=X();z.v=0;z.n=z
for x in xrange(1,50000001):
 for d in xrange(N):p=p.n
 n=X();n.v=x;n.n=p.n;p.n=n;p=n
print z.n.v
