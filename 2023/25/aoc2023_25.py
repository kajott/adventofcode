G,E,F={},{},frozenset
for l in open("input.txt"):
 a,*o=l.replace(':',' ').split()
 for b in o:G[a]=G.get(a,{b})|{b};G[b]=G.get(b,{a})|{a};E[F((a,b))]=0
for p in G:
 v,q={p},{(p,p)}
 while q:
  v|={z[1]for z in q};q={(b,n)for a,b in q for n in G[b]if(n in v)-1}
  for z in q:E[F(z)]+=1
m=sorted(E.values())[-3]
for(a,b),w in E.items():
 if w>=m:G[a]-={b};G[b]-={a}
v,q={p},{p}
while q:v|=q;q={n for p in q for n in G[p]}-v
n=len(v);print(n*(len(G)-n))
