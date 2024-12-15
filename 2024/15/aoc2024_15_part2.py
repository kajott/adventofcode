E,M=enumerate,{}
for y,l in E(f:=open("input.txt")):
 if'#'>l:break
 for x,c in E(l):M[c]=M.get(c,set())|{2*x+y*1j}
W,B,C={p+e for p in M['#']for e in(0,1)},M['O'],M['@'].pop()
N=lambda*u:{p+e for p in b for e in u}
for c in''.join(l.strip()for l in f):
 o=d={'<':-1,'>':1,'^':-1j,'v':1j}[c];b={C+d-1,C+d}&B
 while o!=b:o,b=b,N(0,d-1,d,d+1)&B
 if(C+d in W)+len(N(d,d+1)&W)<1:B=B-b|N(d);C+=d
print(sum(int(p.real+p.imag*100)for p in B))
