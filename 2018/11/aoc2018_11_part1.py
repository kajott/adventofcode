import itertools as I
S=7989
g=[[((x+11)*(y+1)+S)*(x+11)/100%10-5 for x in xrange(300)] for y in xrange(300)]
r=range(297);print max((sum(sum(g[y+i][x:x+3]) for i in range(3)),x+1,y+1) for x,y in I.product(r,r))[1:]
