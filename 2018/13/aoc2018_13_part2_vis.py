import sys
t=[list(r.rstrip()) for r in r'''
/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/
'''.strip('\n').split('\n')]
def V():
 u=c[::-1]
 print
 for y,r in enumerate(t):
  l=""
  for x,b in enumerate(r):
   if u and u[-1][:2]==(y,x):
    l+={(-1,0):'<',(1,0):'>',(0,-1):'^',(0,1):'v'}.get(tuple(u.pop()[2:4]),'?')
   else:l+=b
  print l
 print
c,i=[],999
for y,r in enumerate(t):
 for x,p in enumerate(r):
  h,v,b={'<':(-1,0,'-'),'>':(1,0,'-'),'^':(0,-1,'|'),'v':(0,1,'|')}.get(p,(0,0,0))
  if b:t[y][x]=b;c.append((y,x,h,v,-1))
while 1:
 if i>=len(c):
  V()
  if len(c)<2:break
  i=0;c.sort()
 y,x,h,v,d=c[i];y+=v;x+=h;b=t[y][x];r=0
 z=[j for j,q in enumerate(c) if q[:2]==(y,x)]
 if z:
  print "collision at",(x,y)
  c=[q for j,q in enumerate(c) if j!=i and j!=z[0]];i-=z[0]<i
 else:
  if b=='+':r=d;d=d+1-3*(d>0)
  elif b=='/':r=1-2*(v==0)
  elif b=='\\':r=1-2*(h==0)
  if r:h,v=-r*v,r*h
  c[i]=(y,x,h,v,d)
  i+=1
print c[0][:2][::-1]
