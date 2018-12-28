_=enumerate
t,c,i=[list(r.rstrip())for r in open("input.txt")],[],0
for y,r in _(t):
 for x,p in _(r):
  h,v,b={'<':(-1,0,'-'),'>':(1,0,'-'),'^':(0,-1,'|'),'v':(0,1,'|')}.get(p,(0,0,0))
  if b:t[y][x]=b;c+=[(y,x,h,v,-1)]
while 1:
 l=len(c)
 if i>=l:
  if l<2:break
  i=0;c.sort()
 y,x,h,v,d=c[i];y+=v;x+=h;b=t[y][x];r=0
 z=[j for j,q in _(c)if q[:2]==(y,x)]
 if z:c=[q for j,q in _(c)if j!=i and j!=z[0]];i-=z[0]<i
 else:
  if'+'==b:r=d;d=d+1-3*(d>0)
  elif'/'==b:r=1-2*(v==0)
  elif'\\'==b:r=1-2*(h==0)
  if r:h,v=-r*v,r*h
  c[i]=(y,x,h,v,d);i+=1
print c[0][:2][::-1]
