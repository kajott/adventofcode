_=enumerate
from collections import*
t,l=[],""
for y,r in _(open("input.txt")):t+=[(x+y*1j,c)for x,c in _(r)if' '<c]
p=t[0][0];d=1j;t=defaultdict(int,t)
while t[p]:
 if'@'<t[p]<'|':l+=t[p]
 if t[p+d]<1:
  if t[p+d*1j]:d*=1j
  elif t[p-d*1j]:d*=-1j
 p+=d
print l
