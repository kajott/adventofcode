e=0
for l in open("input.txt"):
 s=[]
 for c in l:
  c={'(':-1,')':1,'[':-2,']':2,'{':-3,'}':3,'<':-4,'>':4}.get(c,0)
  if c<0:s+=[-c]
  else:
   z=s.pop()
   if z!=c:break
 e+=[0,3,57,1197,25137][c]
print e
