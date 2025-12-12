E,R,G=enumerate,range,0
for L in open("input.txt"):
 L=[x[1:-1]for x in L.split()];s,t,p=9,sum(1<<b for b,c in E(L[0])if'.'>c),[sum(1<<int(b)for b in p.split(','))for p in L[1:-1]]
 for m in R(1<<len(p)):
  r=t
  for b,x in E(p):r^=x*(m>>b&1)
  if r<1:s=min(s,sum(m>>b&1 for b in R(23)))
 G+=s
print(G)
