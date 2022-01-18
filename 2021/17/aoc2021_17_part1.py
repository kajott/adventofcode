import re
A,B,C,D=map(int,re.findall('-?\d+',open("input.txt").read()))
H=0
for i in range(99):
 for j in range(99):
  x=y=h=0;u,v=i,j
  while y>=C:
   if(y<=D)*(A<=x<=B):H=max(H,h);break
   h=max(h,y);x+=u;y+=v;u-=u>0;v-=1
print H
