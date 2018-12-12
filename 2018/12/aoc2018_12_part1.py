import re
f=open("input.txt")
C=lambda c:int(c=='#')
b=4*[0]
s=b+map(C,f.readline()[15:].strip())+b
m=dict((tuple(map(C,p)),C(r)) for p,r in re.findall('([.#]+) => ([.#])',f.read()))
for g in xrange(20):s=b+[m[tuple(s[i:i+5])] for i in xrange(len(s)-5)]+b
print sum(i-44 for i,x in enumerate(s) if x)
