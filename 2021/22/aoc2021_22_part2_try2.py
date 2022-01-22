import re
C=[]
for l in open("input.txt"):
 n=[int(x)+(i&1)for i,x in enumerate(re.findall('-?\d+',l))]
 for x in range(6):
  o=C;C=[]
  for c in o:d=c[:];e=c[:];d[x&6]=e[x|1]=n[x];C+=[d,e]if(c[x&6]<n[x]<c[x|1])*all((c[a]<=n[a+1])*(n[a]<=c[a+1])for a in(0,2,4))else[c]
 C=[c for c in C if any((n[a]>c[a])+(c[a+1]>n[a+1])for a in(0,2,4))]+[n]*('f'<l[1])
print sum((b-a)*(d-c)*(f-e)for a,b,c,d,e,f in C)
