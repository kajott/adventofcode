E,M=enumerate,{}
for y,l in E(f:=open("input.txt")):
 if'#'>l:break
 for x,c in E(l):M[c]=M.get(c,set())|{x+y*1j}
W,B,C=M['#'],M['O'],M['@'].pop()
for c in''.join(l.strip()for l in f):
 d={'<':-1,'>':1,'^':-1j,'v':1j}[c];n=e=C+d
 while e in B:e+=d
 if(e in W)-1:
  if e-n:B=B-{n}|{e}
  C=n
print(sum(int(p.real+p.imag*100)for p in B))
