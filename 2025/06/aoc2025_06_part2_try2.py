T=[*open("input.txt")]
O=T.pop().split()
P=lambda z:z and z[0]*P(z[1:])or 1
s,n=0,[]
for x in(''.join(r).strip()for r in zip(*T)):
 if x:n+=[int(x)]
 else:s+=(P if'+'>O.pop(0)else sum)(n);n=[]
print(s)
