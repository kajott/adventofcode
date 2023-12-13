E=enumerate;M={y*1j+x:c for y,r in E(open("input.txt"))for x,c in E(r)}
A,S=0,[p for p,c in M.items()if'S'==c][0]
for d in(1,-1,1j,-1j):
 p,t=S,0
 while A<1:
  t+=1;p+=d
  if p==S:A=t//2
  r={'|':(1j,1j),'-':(1,1),'L':(1j,1),'J':(1j,-1),'F':(-1,1j),'7':(1,1j)}.get(M[p],(0,0))
  if d==r[0]:d=r[1]
  elif d==-r[1]:d=-r[0]
  else:break
print(A)
