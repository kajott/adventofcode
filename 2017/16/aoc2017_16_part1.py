p=map(chr,range(97,113))
for a in open("input.txt").read().strip().split(','):
 c=a[0];a=a[1:].split('/')
 if's'==c:a=-int(a[0]);p=p[a:]+p[:a]
 else:a,b=map(int,a)if c>'p'else(p.index(x)for x in a);p[a],p[b]=p[b],p[a]
print''.join(p)
