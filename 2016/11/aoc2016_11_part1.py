_=enumerate
import re
e,o={},[]
def a(n):e[n]=x=e.get(n,len(e)*2);return x
for f,l in _(open("input.txt")):o+=[(a(n)+(t<'-'),3-f)for n,t in re.findall(r'(\w+)(-| g)',l)]
s=tuple([f for d,f in sorted(o)]+[3])
N,c,q,v,d,r=len(o),{s},set(),{s},1,0
while r<1:
 if not c:c=q;q=set();d+=1
 s=c.pop()
 for a in[i for i in range(N)if s[i]==s[-1]]:
  for b in[i for i in range(a,N)if s[i]==s[-1]]:
   for p in(1,-1):
    p+=s[-1]
    if p&4:continue
    n=list(s);n[a]=n[b]=n[-1]=p;n=tuple(n)
    if sum(n)<1:r=d
    if n in v:continue
    g={i for i,f in _(n[1::2])if f==p}
    if not(g and {i for i,f in _(n[:N:2])if f==p}-g):q|={n};v|={n}
print r
