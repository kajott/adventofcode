N=33100000/10
S=lambda x:sum(d+(x/d)*(d*d!=x)for d in xrange(1,int(x**0.5+1))if x%d<1)
x=99999
while S(x+9)<N:x+=9
while S(x)<N:x+=1
print x
