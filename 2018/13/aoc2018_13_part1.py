_=enumerate
import sys
t,c=[list(r.rstrip())for r in open("input.txt")],[]
for y,r in _(t):
 for x,p in _(r):
  h,v,b={'<':(-1,0,'-'),'>':(1,0,'-'),'^':(0,-1,'|'),'v':(0,1,'|')}.get(p,(0,0,0))
  if b:t[y][x]=b;c+=[(y,x,h,v,-1)]
while 1:
 c.sort()
 for i,q in _(c):
  y,x,h,v,d=q;y+=v;x+=h;b=t[y][x];r=0
  if any(q[:2]==(y,x)for q in c):print(x,y);sys.exit(0)
  if b=='+':r=d;d=d+1-3*(d>0)
  elif b=='/':r=1-2*(v==0)
  elif b=='\\':r=1-2*(h==0)
  if r:h,v=-r*v,r*h
  c[i]=(y,x,h,v,d)
