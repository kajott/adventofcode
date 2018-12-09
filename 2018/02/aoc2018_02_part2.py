x=map(str.strip, open("input.txt"))
for p in xrange(len(x[0])):
 s=set()
 for f in x:
  k=f[:p]+f[p+1:]
  if k in s:print k;break
  s.add(k)
