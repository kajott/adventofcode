T=[*open("input.txt")]
O=T.pop().split()
s,n=0,[]
for x in(''.join(r).strip()for r in zip(*T)):
 if x:n+=[x]
 else:s+=eval(O.pop(0).join(n));n=[]
print(s)
