import re
G={}
for l in open("input.txt"):
 c=[map(int,k)for k in re.findall('(\d+),(\d+)',l)];x,y=c[0];G[x+y*1j]=1
 for q,p in c:
  while(q-x)|(p-y):x+=(x<q)-(x>q);y+=(y<p)-(y>p);G[x+y*1j]=1
N=f=0
while f-1:
 G[p]=2;p=500;f=1;N+=1
 while(p.imag<200)*f:
  f=0
  for n in(p+1j,p-1+1j,p+1+1j):
   if(n in G)-1:f=1;p=n;break
print N-1
