E=enumerate;M={y*1j+x:c for y,r in E(open("input.txt"))for x,c in E(r)}
V,S,D=[],[p for p,c in M.items()if'S'==c][0],{1,-1,1j,-1j}
for d in D:
 z,q=[{-1},{-1},{-1}],S
 while[]<=V:
  p=q;z[0]|={p};q+=d
  for s in(1,-1):z[s]|={k+s*d*1j for k in(p,q)}
  if q==S:V=z
  r={'|':(1j,1j),'-':(1,1),'L':(1j,1),'J':(1j,-1),'F':(-1,1j),'7':(1,1j)}.get(M[q],(0,0))
  if d==r[0]:d=r[1]
  elif d==-r[1]:d=-r[0]
  else:break
for n in V[1:]:
 c=1;D|={0}
 while(n!=z)*c:z=n;n={p+d for p in n-V[0]for d in D};c=(0 in n)-1
 if c:print(len(n-V[0]))
