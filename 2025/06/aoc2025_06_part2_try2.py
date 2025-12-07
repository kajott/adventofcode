import math
T=[*open("input.txt")]
O=T.pop().split()
s,n=0,[]
for x in(''.join(r).strip()for r in zip(*T)):
 if x:n+=[int(x)]
 else:s+=(math.prod if'+'>O.pop(0)else sum)(n);n=[]
print(s)
