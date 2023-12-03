import re
N,O=[],[]
for y,l in enumerate(open("input.txt")):
 for m in re.finditer('\d+|[^.]',l.strip()):
  s,e,c=m.start(0),m.end(0),m.group(0)
  if'0'<c<':':N+=[(y,s,e,int(c))]
  else:O+=[(y,s)]
V=lambda v,u:([(y,e,n)for y,s,e,n in N if(y==v)*(s<=u<e)]or[(0,0,0)]).pop()
print(sum(z[2]for z in{V(y+v,x+u)for y,x in O for u in(-1,0,1)for v in(-1,0,1)}))
