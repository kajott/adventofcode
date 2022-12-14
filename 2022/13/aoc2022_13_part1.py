A=[eval(l)for l in open("input.txt")if l.strip()]
I=lambda _:type(_)==int
def C(a,b):
 if I(a)*I(b):return a-b
 if I(a):a=[a]
 if I(b):b=[b]
 for x,y in zip(a,b):
  r=C(x,y)
  if r:return r
 return len(a)-len(b)
print sum((i/2+1)*(C(A[i],A[i+1])<0)for i in range(0,len(A),2))
