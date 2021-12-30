e=[]
for l in open("input.txt"):
 s,f=[],0
 for c in l.strip():
  c={'(':-1,')':1,'[':-2,']':2,'{':-3,'}':3,'<':-4,'>':4}[c]
  if c<0:s+=[-c]
  else:
   z=s.pop()
   if z!=c:s=[];break
 for i in s[::-1]:f=f*5+i
 if f:e+=[f]
e.sort()
print e[len(e)/2]
