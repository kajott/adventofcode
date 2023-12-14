R,O,M,E=0,[],{},enumerate
for L,r in E(open("input.txt")):
 for x,c in E(r):p=L+1j*x;M[p]=c in"O.";O+=[p]*('A'<c)
for p in O:
 while M.get(p-1):p-=1
 M[p]=0;R+=L+1-int(p.real)
print(R)
