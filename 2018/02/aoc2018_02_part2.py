x=map(str.strip,open("input.txt"))
for p in range(len(x[0])):
 s={0}
 for f in x:
  k=f[:p]+f[p+1:]
  if k in s:print k;break
  s|={k}
