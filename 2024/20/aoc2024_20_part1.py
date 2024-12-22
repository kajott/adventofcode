E,M=enumerate,{}
for y,l in E(open("input.txt")):
 for x,c in E(l):M[c]=M.get(c,set())|{x+y*1j}
F=M['.']|M['E']
I=(1,-1,1j,-1j)
D,q,t={},{M['S'].pop()},0
while q:
 for p in q:D[p]=t
 t+=1;q={p+e for p in q for e in I}&F-{*D}
print(sum(99<D.get(p+d+d,0)-2-D[p]for p in D for d in I))
