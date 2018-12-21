_=range
import re
v=[map(int,re.findall('\d+',x))for x in open("input.txt")]
s,t=(min(p[i]for p in v)-1for i in(0,1))
w,h=(max(p[i]for p in v)+1for i in(0,1))
r=[0]*len(v)
for y in _(t,h+1):
 for x in _(s,w+1):
  d=sorted((abs(x-p[0])+abs(y-p[1]),i)for i,p in enumerate(v))
  if d[0][0]<d[1][0]:r[d[0][1]]+=1-999*(x<=s or y<=t or x>=w or y>=h)
print max(r)
