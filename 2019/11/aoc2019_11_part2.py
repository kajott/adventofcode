from collections import*
_,G,z,r,d=int,{0:1},1,0,-1j
M=defaultdict(_,enumerate(map(_,open("input.txt").read().split(','))));p=s=0
while M[p]!=99:
 o=M[p];l=map(_,str(o)[-3::-1]+"000");o%=100;n=_("0331122331"[o]);i,j,k=[M[p+x]+s*(m>1)for x,m in zip((1,2,3),l)];a,b=[(M[x]if m-1else x)for x,m in zip((i,j),l)];p+=n+1
 if o<2:M[k]=a+b
 elif o<3:M[k]=a*b
 elif o<4:M[i]=G.get(r,0)
 elif o<5:
  if z:G[r]=a
  else:d*=(2*a-1)*1j;r+=d
  z^=1
 elif o>8:s+=a
 elif o>7:M[k]=a==b
 elif o>6:M[k]=a<b
 elif(o>5)^(a!=0):p=b
for y in range(6):print''.join(" #"[G.get(x+y*1j,0)]for x in range(80))
