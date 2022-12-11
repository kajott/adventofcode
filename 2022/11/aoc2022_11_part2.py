import re
I=re.findall('\d+|old.*',open("input.txt").read())
V,M,G=lambda:[int(I.pop(0))],[],1
while I:
 m=[0,[]];V()
 while'@'>I[0]:m[1]+=V()
 m+=[I.pop(0)]+V()+V()+V();G*=m[3];M+=[m]
for r in range(10000):
 for m in M:
  while m[1]:m[0]+=1;old=m[1].pop(0);v=eval(m[2])%G;M[m[5-(v%m[3]==0)]][1]+=[v]
a,b=sorted(m[0]for m in M)[-2:];print a*b
