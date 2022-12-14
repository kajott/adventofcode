import re
G={0};M=0
for l in open("input.txt"):
 c=[map(int,k)for k in re.findall('(\d+),(\d+)',l)];x,y=c[0];G|={x+y*1j}
 for q,p in c:
  while(q-x)|(p-y):x+=(x<q)-(x>q);y+=(y<p)-(y>p);G|={x+y*1j};M=max(M,y)
a=c={500}
for _ in range(M+1):
 n=set()
 for d in(-1,0,1):n|={p+d+1j for p in c}
 c=n-G;a|=c
print len(a)
