import re
F,C,V=frozenset,{},{}
for l in open("input.txt"):m=re.findall('[A-Z]{2}|\d+',l);r=int(m.pop(1));V[m[0]]=(r,m[1:])
def D(*s):
 p,t,v=s;t-=1
 if t<0 or not v:return 0
 if s in C:return C[s]
 r=(p in v)*(t*V[p][0]+D(p,t,F(set(v)-{p})))
 for q in V[p][1]:r=max(r,D(q,t,v))
 C[s]=r;return r
print D('AA',30,F(p for p in V if V[p][0]))
