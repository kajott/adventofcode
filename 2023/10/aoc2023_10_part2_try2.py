E=enumerate;M={y*1j+x:c for y,r in E(open("input.txt"))for x,c in E(r)}
S,R=[p for p,c in M.items()if'S'==c][0],0
for d in{1,-1,1j,-1j}:
 q=S;a=c=0
 while R<1:
  p=q;q+=d;c+=1;a+=p.real*q.imag-q.real*p.imag
  if q==S:R=(abs(int(a))-c)//2+1
  r={'|':(1j,1j),'-':(1,1),'L':(1j,1),'J':(1j,-1),'F':(-1,1j),'7':(1,1j)}.get(M[q],(0,0))
  if d==r[0]:d=r[1]
  elif d==-r[1]:d=-r[0]
  else:break
print(R)
