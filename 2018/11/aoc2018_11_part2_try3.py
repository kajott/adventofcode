import itertools as I
S=7989
N=300
g=[[((x+11)*(y+1)+S)*(x+11)/100%10-5 for x in xrange(N)] for y in xrange(N)]
def S(d,s):
 r,a=(N-s)*[0],sum(d[:s]);r[0]=a
 for i in xrange(1,N-s):a+=d[i+s-1]-d[i-1];r[i]=a
 return r
def M(s):t=[S(r,s) for r in zip(*(S(r,s) for r in g))];r=xrange(N-s);return max((t[y][x],y+1,x+1,s) for x,y in I.product(r,r))
print max(M(s) for s in xrange(1,N))[1:]
