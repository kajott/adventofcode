T,_=tuple,range
R,P={},lambda p:T(T(c=='#'for c in r)for r in p.strip().split('/'))
for a,b in(map(P,l.split("=>"))for l in open("input.txt")):
 for r in"KeyJ":a=T(zip(*a));R[a]=b;a=T(a[::-1]);R[a]=b
I,z=((0,1,0),(0,0,1),(1,1,1)),3
for t in _(18):
 O=I;s=z;a=2+s%2;b=a+1;z=s/a*b;I=[[]for i in _(z)]
 for y in _(0,s,a):
  for x in _(0,s,a):
   p=R[T(T(O[y+i][x:x+a])for i in _(a))]
   for i in _(b):I[y/a*b+i]+=p[i]
 if t in(4,17):print sum(map(sum,I))
