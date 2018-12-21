_=range
from itertools import*
S=7989
g=[[((x+11)*(y+1)+S)*(x+11)/100%10-5for x in _(300)]for y in _(300)]
r=_(297);print max((sum(sum(g[y+i][x:x+3])for i in _(3)),x+1,y+1)for x,y in product(r,r))[1:]
