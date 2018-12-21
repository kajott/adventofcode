p,o=open("input.txt").read().strip(),0
while o!=p:
 o,i=p,1
 while i<len(p):
  a,b=sorted([p[i-1],p[i]])
  if b.islower()and a==b.upper():p=p[:i-1]+p[i+1:]
  else:i+=1
print len(p)
