M,E={},enumerate
for y,l in E(open("input.txt")):
 for x,c in E(l):M[c]=M.get(c,set())|{x+y*1j}
q,v=[(0,M['S'].pop(),1)],{}
while q:
 s,p,d=q.pop(0)
 if v.get(p,1e9)>s:v[p]=s;q+=[(s+c,p+e,e)for e,c in((d,1),(-d*1j,1001),(d*1j,1001))if(p+e in M['#'])-1]
print(v[M['E'].pop()])
