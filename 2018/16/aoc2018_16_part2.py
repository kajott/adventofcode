import re
O,N=[lambda r,a,b:r[a]+r[b],lambda r,a,b:r[a]+b,lambda r,a,b:r[a]*r[b],lambda r,a,b:r[a]*b,lambda r,a,b:r[a]&r[b],lambda r,a,b:r[a]&b,lambda r,a,b:r[a]|r[b],lambda r,a,b:r[a]|b,lambda r,a,b:r[a],lambda r,a,b:a,lambda r,a,b:a>r[b],lambda r,a,b:r[a]>b,lambda r,a,b:r[a]>r[b],lambda r,a,b:a==r[b],lambda r,a,b:r[a]==b,lambda r,a,b:r[a]==r[b]],range(16)
P,F,r=[set(O)for x in N],{},4*[0]
def C(i,o,f,x,a,b,d):r=i[:];r[d]=f(r,a,b);return r==o
for l in filter(None,(re.findall('(.*?)(\d+) (\d) (\d) (\d)',x.replace(',',''))for x in open("input.txt"))):
 l=l[0];t=l[0][:1];n=map(int,l[1:])
 if t>'A':i=n
 elif t>'@':P[c[0]]-={f for f in O if C(i,n,f,*c)<1};i=0
 elif i:c=n
 else:
  while len(F)<16:
   for j in N:
    p=P[j]-set(F.values())
    if len(p)==1:F[j]=p.pop()
  o,a,b,d=n;r[d]=F[o](r,a,b)
print r[0]
