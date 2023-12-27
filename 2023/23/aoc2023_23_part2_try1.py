E,N,F=enumerate,(1,-1,1j,-1j),{1}
for y,l in E(open("input.txt")):
 for x,c in E(l.strip()):
  if'#'!=c:F|={y*1j+x}
G=y*1j+x-1
J={1,G}|{p for p in F if sum(p+d in F for d in N)>2}
D={j:[]for j in J}
for j in J:
 t,q,v=0,{j},{j}
 while q:
  t+=1;v|=q;q={p+d for p in q for d in N}&F-v
  for p in q&J:D[j]+=[(p,t)]
  q-=J
S=lambda p,v,l:max((S(j,v|{j},l+d)for j,d in D[p]if(j in v)-1),default=0)if p-G else l
print(S(1,{1},0))
