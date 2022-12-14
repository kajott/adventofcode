import re
G={}
for l in open("input.txt"):
 c=[map(int,k)for k in re.findall('(\d+),(\d+)',l)];x,y=c[0];G[(x,y)]=1
 for q,p in c:
  while(q-x)|(p-y):x+=(x<q)-(x>q);y+=(y<p)-(y>p);G[(x,y)]=1
N=f=0
while f-1:
 G[(x,y)]=2;x=500;y=0;f=1;N+=1
 while(y<200)*f:
  f=0
  for n in(x,x-1,x+1):
   if not(n,y+1)in G:f=1;x=n;y+=1;break
print N-1
