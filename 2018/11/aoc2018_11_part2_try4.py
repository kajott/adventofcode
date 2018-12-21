_=range
from itertools import*
S=7989
N=300
t=[[0]*(N+1)]
for y in _(1,N+1):
 t+=[[0]];l=0
 for x in _(1,N+1):l+=((x+10)*y+S)*(x+10)/100%10-5+t[-2][x]-t[-2][x-1];t[-1]+=[l]
print max(max((t[y][x]-t[y-s][x]-t[y][x-s]+t[y-s][x-s],x-s+1,y-s+1,s)for x,y in product(_(s,N+1),_(s,N+1)))for s in _(1,N+1))[1:]
