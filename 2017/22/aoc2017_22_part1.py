_=enumerate
from collections import*
M,n=[],0
for y,r in _(open("input.txt")):M+=[(x,y,c=='#')for x,c in _(r)]
p=max(M);p=p[0]/2-p[1]/2j;d=-1j
M=defaultdict(int,((x+y*1j,c)for x,y,c in M))
for t in range(10000):M[p]=s=1-M[p];d*=(1-2*s)*1j;n+=s;p+=d
print n
