import re
f=open("input.txt")
C=lambda c:int(c=='#')
b=500*[0]
s=b+map(C,f.readline()[15:].strip())+b
m=dict((tuple(map(C,p)),C(r)) for p,r in re.findall('([.#]+) => ([.#])',f.read()))
r=0
for g in xrange(200):
 s=[0,0]+[m[tuple(s[i:i+5])] for i in xrange(len(s)-5)]+3*[0]
 l,r=r,sum(i for i,x in enumerate(s) if x)
print r+49999999800*(r-l)-500*sum(s)
