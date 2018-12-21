_=range
from itertools import*
S=7989
N=300
g=[[((x+11)*(y+1)+S)*(x+11)/100%10-5for x in _(N)]for y in _(N)]
def M(s):r=_(N-s);return max((sum(sum(g[y+i][x:x+s])for i in _(s)),x+1,y+1,s)for x,y in product(r,r))
b=(0,)
for s in _(1,N):b=max(b,M(s));print b[1:]
