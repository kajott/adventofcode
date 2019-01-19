N=3014603
class X:pass
p=c=X();c.i=1
for i in range(2,N+1):
 n=X();n.i=i;c.n=n;c=n
 if i==N/2:h=c
c.n=p
for c in range(2,N):
 if c&1:h=h.n
 h.n=h.n.n;p=p.n
print p.i
