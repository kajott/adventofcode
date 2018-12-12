import itertools as I
S=7989
N=300
g=[[((x+11)*(y+1)+S)*(x+11)/100%10-5 for x in xrange(N)] for y in xrange(N)]
S=lambda r,s:[sum(r[x:x+s]) for x in xrange(N-s)]
def M(s):t=[S(r,s) for r in zip(*(S(r,s) for r in g))];r=xrange(N-s);return max((t[y][x],y+1,x+1,s) for x,y in I.product(r,r))
print max(M(s) for s in xrange(1,N))[1:]
