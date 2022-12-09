I=open("input.txt").read().split()
p=[(0,0)]*9;z={0};s=t=0
while I:
 d=ord(I.pop(0));j=2*(d>80)-1;i=(d/3&1)*j
 for k in range(int(I.pop(0))):
  u,v=s,t=s+i,t+j-i
  for l in range(9):x,y=p[l];c=abs(x-u)>1or abs(y-v)>1;x+=c*((x<u)-(x>u));y+=c*((y<v)-(y>v));p[l]=u,v=x,y
  z|={(x,y)}
print len(z)-1
