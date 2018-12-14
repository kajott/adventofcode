import sys
t=[list(r.rstrip()) for r in r'''
/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   
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
c=[]
for y,r in enumerate(t):
 for x,p in enumerate(r):
  h,v,b={'<':(-1,0,'-'),'>':(1,0,'-'),'^':(0,-1,'|'),'v':(0,1,'|')}.get(p,(0,0,0))
  if b:t[y][x]=b;c.append((y,x,h,v,-1))
while 1:
 c.sort()
 V()
 for i,q in enumerate(c):
  y,x,h,v,d=q
  print i,q,
  y+=v;x+=h;b=t[y][x];r=0
  print '->',y,x,
  assert b!=' '
  assert b!='-' or h
  assert b!='|' or v
  if any(q[:2]==(y,x) for q in c):print;print (x,y);sys.exit(0)
  if b=='+':r=d;d=d+1-3*(d>0)
  elif b=='/':r=1-2*(v==0)
  elif b=='\\':r=1-2*(h==0)
  print r
  if r:h,v=-r*v,r*h
  c[i]=(y,x,h,v,d)
