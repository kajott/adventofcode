import re;A,R=abs,range
M,S=4000000,0;E=[[]for x in R(M)]
for x,y,u,v in(map(int,re.findall('-?\d+',l))for l in open("input.txt")):
 d=A(x-u)+A(y-v);S+=1
 for z in R(max(0,y-d),min(M,y+d)):w=d-A(z-y);E[z]+=[(max(0,x-w),-S),(min(M,x+w)+1,S)]
for y in R(M):
 a=set();e=M
 for x,i in sorted(E[y]):
  if i>0:a-={i};e=a and e or x
  else:
   if x==e+1and not a:print M*e+y
   a|={-i}
