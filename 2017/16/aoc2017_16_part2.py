D=open("input.txt").read().strip().split(',')
h,t,p={0:0},0,map(chr,range(97,113))
while 1:
 k=''.join(p)
 if k==h[0]:break
 h[t]=k;t+=1
 for a in D:
  c=a[0];a=a[1:].split('/')
  if's'==c:a=-int(a[0]);p=p[a:]+p[:a]
  else:a,b=map(int,a)if c>'p'else(p.index(x)for x in a);p[a],p[b]=p[b],p[a]
print h[10**9%t]
