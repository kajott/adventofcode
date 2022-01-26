import re
z=map(int,re.findall('-?\d+',open("input.txt").read()))
I,D,M,A=0,z[2::10],z[3::10],z[9::10]
while z:
 I+=1;z=n=0;d=9**6
 for r in range(14):
  c=z%26+M[r]
  if 0<c<=9:w=c
  elif D[r]>1:z=1;break
  else:w=1+I/d%9;d/=9
  n=n*10+w;z/=D[r]
  if c-w:z=z*26+w+A[r]
print n
