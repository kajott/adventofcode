H,O,M,E=[],[],{},enumerate
for L,r in E(open("input.txt")):
 for x,c in E(r):p=L*1j+x;M[p]=c in"O.";O+=[p]*('A'<c)
def R(d):
 O.sort(key=lambda p:-d.real*p.real-d.imag*p.imag);f=dict(M)
 for i,p in E(O):
  while f.get(p+d):p+=d
  O[i]=p;f[p]=0
while(O in H)-1:H+=[O[:]];R(-1j);R(-1);R(1j);R(1)
t=len(H);p=t-H.index(O);print(sum(L+1-int(p.imag)for p in H[(int(1E9)-t)%p-p]))
