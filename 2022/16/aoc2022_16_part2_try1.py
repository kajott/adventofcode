import re
F,C,V=frozenset,{},{}
for l in open("input.txt"):m=re.findall('[A-Z]{2}|\d+',l);r=int(m.pop(1));V[m[0]]=(r,m[1:])
def D(C,N,*s):
 p,t,v=s;t-=1
 if not v:return 0
 if t<0:return N and D(N,0,'AA',26,v)
 if s in C:return C[s]
 r=(p in v)*(t*V[p][0]+D(C,N,p,t,F(set(v)-{p})))
 for q in V[p][1]:r=max(r,D(C,N,q,t,v))
 C[s]=r;return r
print D({0:0},{0:0},'AA',26,F(p for p in V if V[p][0]))
