p=open("input.txt").read().strip()
def r(p):
 i=0
 while i<len(p)-1:
  a,b=sorted([p[i],p[i+1]])
  if b.islower() and a==b.upper():
   p=p[:i]+p[i+2:]
   i=max(0,i-1)
  else:i+=1
 return len(p)
print min(r(p.translate(None,c+c.lower())) for c in map(chr,xrange(65,91)))
