_=enumerate
from collections import*
M,n=[],0
for y,r in _(open("input.txt")):M+=[(x,y,2*(c=='#'))for x,c in _(r)]
p=max(M);p=p[0]/2-p[1]/2j;d=-1j
M=defaultdict(int,((x+y*1j,c)for x,y,c in M))
for t in range(10**7):M[p]=s=(M[p]+1)&3;d*=-1j**s;n+=(s==2);p+=d
print n
