_=range
import re,collections as C
d,a=C.defaultdict(set),[0]
for i,x,y,w,h in(map(int,re.findall('\d+',x))for x in open("input.txt")):
 a+=[w*h]
 for y in _(y,y+h):
  for j in _(x,x+w):d[(j,y)]|={i}
for s in d.values():
 if len(s)==1:a[s.pop()]-=1
print[i for i,a in enumerate(a)if a<1][1]
