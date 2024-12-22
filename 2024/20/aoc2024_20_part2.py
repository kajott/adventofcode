E,M=enumerate,{}
for y,l in E(open("input.txt")):
 for x,c in E(l):M[c]=M.get(c,set())|{x+y*1j}
F,A=M['.']|M['E'],abs
I={(x+y*1j,A(x)+A(y))for x in range(-20,21)for y in range(A(x)-20,21-A(x))}
D,q={},{M['S'].pop()};t=r=0
while q:
 for p in q:D[p]=t
 t+=1;q={p+e for p in q for e in(1,-1,1j,-1j)}&F-{*D}
print(sum(99<D.get(p+d,0)-x-D[p]for p in D for d,x in I))
