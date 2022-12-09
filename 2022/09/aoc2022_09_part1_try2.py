I=open("input.txt").read().split()
D=lambda d:(d<0)-(d>0)
h=t=0;z={0}
while I:
 d=ord(I.pop(0));j=2*(d>80)-1;i=(d/3&1)*j;d=j-i+i*1j
 for k in range(int(I.pop(0))):h+=d;a=t-h;t+=(abs(a)>=2)*(D(a.real)+1j*D(a.imag));z|={t}
print len(z)
