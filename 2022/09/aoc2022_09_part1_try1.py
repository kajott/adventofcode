I=open("input.txt").read().split()
x=y=u=v=0;z={0}
while I:
 d=ord(I.pop(0));j=2*(d>80)-1;i=(d/3&1)*j
 for k in range(int(I.pop(0))):u+=i;v+=j-i;c=abs(x-u)>1or abs(y-v)>1;x+=c*((x<u)-(x>u));y+=c*((y<v)-(y>v));z|={(x,y)}
print len(z)-1
