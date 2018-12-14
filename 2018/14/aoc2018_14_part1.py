N=640441
r,p,l=[3,7],[0,1],2
while l<N+10:
 s=r[p[0]]+r[p[1]]
 if s>9:r+=[1]
 r+=[s%10];l=len(r);p=[(x+r[x]+1)%l for x in p]
print ''.join(map(str,r[N:N+10]))
