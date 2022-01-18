import re
A,B,C,D=map(int,re.findall('-?\d+',open("input.txt").read()))
N=0
for i in range(B+1):
 for j in range(C,99):
  x=y=0;u,v=i,j
  while y>=C:
   if(y<=D)*(A<=x<=B):N+=1;break
   x+=u;y+=v;u-=u>0;v-=1
print N
