M,E={},enumerate
for y,l in E(open("input.txt")):
 for x,c in E(l):M[c]=M.get(c,set())|{x+y*1j}
E,q,v,b=M['E'].pop(),[(0,M['S'].pop(),1,set())],{},{}
while q:
 s,p,d,t=q.pop(0)
 if p==E:b[s]=b.get(s,{E})|t
 if v.get((p,d),1e9)>=s:v[(p,d)]=s;q+=[(s+c,p+e,e,t|{p})for e,c in((d,1),(-d*1j,1001),(d*1j,1001))if(p+e in M['#'])-1]
print(m:=min(b))
print(len(b[m]))
