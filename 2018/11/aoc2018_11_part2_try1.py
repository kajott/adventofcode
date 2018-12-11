import itertools as I
S=7989
N=300
g=[[((x+11)*(y+1)+S)*(x+11)/100%10-5 for x in xrange(N)] for y in xrange(N)]
def M(s):r=range(N-s);return max((sum(sum(g[y+i][x:x+s]) for i in xrange(s)),x+1,y+1,s) for x,y in I.product(r,r))
b=(0,)
for s in xrange(1,N):b=max(b,M(s));print b[1:]
