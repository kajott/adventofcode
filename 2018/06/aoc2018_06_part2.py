_=range
import re
r,v=0,[map(int,re.findall('\d+',x))for x in open("input.txt")]
s,t=(min(p[i]for p in v)for i in(0,1))
w,h=(max(p[i]for p in v)+1for i in(0,1))
for y in _(t,h):
 for x in _(s,w):
  if sum(abs(x-a)+abs(y-b)for a,b in v)<10000:r+=1
print r
