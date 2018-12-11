import itertools as I
S=7989
N=300
t=[[0]*(N+1)]
for y in xrange(1,N+1):
 t.append([0]);l=0
 for x in xrange(1,N+1):l+=((x+10)*y+S)*(x+10)/100%10-5+t[-2][x]-t[-2][x-1];t[-1].append(l)
print max(max((t[y][x]-t[y-s][x]-t[y][x-s]+t[y-s][x-s],x-s+1,y-s+1,s) for x,y in I.product(range(s,N+1),range(s,N+1))) for s in xrange(1,N+1))[1:]
