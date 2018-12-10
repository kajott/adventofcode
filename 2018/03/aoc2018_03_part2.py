import re,collections as C
d=C.defaultdict(set)
a=[0]
for i,x,y,w,h in (map(int,re.findall('\d+',x)) for x in open("input.txt")):
 a.append(w*h)
 for y in xrange(y,y+h):
  for j in xrange(x,x+w):d[(j,y)].add(i)
for s in d.values():
 if len(s)==1:a[s.pop()]-=1
print [i for i,a in enumerate(a) if a==0][1]
