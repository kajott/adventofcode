_=range
import re
d={}
for i,x,y,w,h in(map(int,re.findall('\d+',x))for x in open("input.txt")):
 for y in _(y,y+h):
  for j in _(x,x+w):d[(j,y)]=d.get((j,y),0)+1
print sum(v>1for v in d.values())
