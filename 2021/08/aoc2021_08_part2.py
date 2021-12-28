s,M=0,{}
C=lambda s:''.join(sorted(s))
def A(n,l,c=lambda _:1):p=[p for p in P if c(p)and len(p)==l].pop();M[C(p)]=str(n);return p
for l in open("input.txt"):P,N=(map(set,p.split())for p in l.split('|'));A(8,7);A(7,3);x=A(1,2);y=A(4,4);z=A(3,5,lambda _:_>x);b=y-z;x=A(5,5,lambda _:_>b);y=A(2,5,lambda _:_!=z and _!=x);c=z-x;e=y-z;x=A(6,6,lambda _:(_>c)-1);y=A(9,6,lambda _:(_>e)-1);A(0,6,lambda _:_!=x and _!=y);s+=int(''.join(M[C(p)]for p in N))
print s
