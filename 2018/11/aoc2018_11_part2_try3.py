_=range
from itertools import*
S=7989
N=300
g=[[((x+11)*(y+1)+S)*(x+11)/100%10-5for x in _(N)]for y in _(N)]
def S(d,s):
 r,a=(N-s)*[0],sum(d[:s]);r[0]=a
 for i in _(1,N-s):a+=d[i+s-1]-d[i-1];r[i]=a
 return r
def M(s):t=[S(r,s)for r in zip(*(S(r,s)for r in g))];r=_(N-s);return max((t[y][x],y+1,x+1,s)for x,y in product(r,r))
print max(M(s)for s in _(1,N))[1:]
