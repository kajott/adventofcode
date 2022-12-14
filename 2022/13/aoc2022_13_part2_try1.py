A=[eval(l)for l in open("input.txt")if l.strip()]+[2,6]
I=lambda _:type(_)==int
def C(a,b):
 if I(a)*I(b):return a-b
 if I(a):a=[a]
 if I(b):b=[b]
 for x,y in zip(a,b):
  r=C(x,y)
  if r:return r
 return len(a)-len(b)
A=[0]+sorted(A,C)
print A.index(2)*A.index(6)
