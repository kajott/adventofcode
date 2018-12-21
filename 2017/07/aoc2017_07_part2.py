import re,sys,collections as C
F=re.findall
w,t,u={},{},[]
for l in open("input.txt"):c=F('[a-z]+',l);n=c.pop(0);t[n]=c;u+=c;w[n]=int(F('\d+',l)[0])
def B(r):
 d=C.defaultdict(list)
 for s in t[r]:d[B(s)]+=[s]
 i=d.items()
 if len(d)>1:f=sorted((len(b),a)for a,b in i);z=f[0][1];print w[d[z][0]]-z+f[1][1];sys.exit(0)
 return sum(a*len(b)for a,b in i)+w[r]
B(list(set(w)-set(u))[0])
