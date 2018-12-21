import re
n,m=map(int,re.findall('\d+',open("input.txt").read()))
class S:pass
c=S();c.i,c.p,c.n,s=0,c,c,n*[0]
for i in range(1,m*100+1):
 if i%23:c=c.n;x=S();x.i,x.p,x.n=i,c,c.n;x.n.p,x.p.n,c=x,x,x
 else:c=c.p.p.p.p.p.p.p;s[i%n]+=i+c.i;c.p.n,c.n.p,c=c.n,c.p,c.n
print max(s)
