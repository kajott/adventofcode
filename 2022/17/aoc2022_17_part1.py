J=open("input.txt").read().strip();P,L=0,len(J)
S=[[60],[16,56,16],[56,8,8],[32]*4,[48]*2]
F,H=9999*[257]+[-1],0
for _ in range(2022):
 s=S.pop(0);S+=[s];e=len(s);r=range(e);y=H+3;f=1
 while f:
  t=[z<<1if'>'>J[P%L]else z>>1for z in s]
  if any(F[y+i]&t[i]for i in r)-1:s=t
  P+=1;f=any(F[y-1+i]&s[i]for i in r)-1;y+=f
 for i in r:F[y+i]|=s[i]
 H=max(H,y+e)
print H
