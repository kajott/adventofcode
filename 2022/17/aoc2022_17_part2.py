J=open("input.txt").read().strip();P,L=0,len(J)
S=[[60],[16,56,16],[56,8,8],[32]*4,[48]*2]
F,T=999999*[257]+[-1],int(1E12);H=R=Z=0
while R<T:
 s=S.pop(0);S+=[s];e=len(s);r=range(e);y=H+3;f=1
 while f:
  t=[z<<1if'>'>J[P%L]else z>>1for z in s]
  if any(F[y+i]&t[i]for i in r)-1:s=t
  P+=1;f=any(F[y-1+i]&s[i]for i in r)-1;y+=f
 for i in r:F[y+i]|=s[i]
 H=max(H,y+e);R+=1
 if P>L*5and Z<1:T-=R;Z=H;A,R=H,0
 if P>L*10and T>1E6:d=T/R;T-=d*R;Z+=d*(H-A);A,R=H,0
print Z+H-A
