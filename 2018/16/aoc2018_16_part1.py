import re
O,r=[lambda r,a,b:r[a]+r[b],lambda r,a,b:r[a]+b,lambda r,a,b:r[a]*r[b],lambda r,a,b:r[a]*b,lambda r,a,b:r[a]&r[b],lambda r,a,b:r[a]&b,lambda r,a,b:r[a]|r[b],lambda r,a,b:r[a]|b,lambda r,a,b:r[a],lambda r,a,b:a,lambda r,a,b:a>r[b],lambda r,a,b:r[a]>b,lambda r,a,b:r[a]>r[b],lambda r,a,b:a==r[b],lambda r,a,b:r[a]==b,lambda r,a,b:r[a]==r[b]],0
def C(i,o,f,x,a,b,d):r=i[:];r[d]=f(r,a,b);return r==o
for l in filter(None,(re.findall('(.*?)(\d+) (\d) (\d) (\d)',x.replace(',','')) for x in open("input.txt"))):
 l=l[0];t=l[0][:1];n=map(int,l[1:])
 if t=='B':i=n
 elif t=='A':r+=sum(C(i,n,f,*c) for f in O)>2;i=0
 elif i:c=n
print r
