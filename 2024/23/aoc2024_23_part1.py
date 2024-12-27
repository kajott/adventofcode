C,T={},{}
for l in open("input.txt"):a,b=map(str.strip,l.split('-'));C[a]=C.get(a,{b})|{b};C[b]=C.get(b,{a})|{a}
for a in C:
 for b in C[a]:
  for c in C[a]:
   if(b!=c)*(c in C[b]):T[tuple(sorted((a,b,c)))]=0
print(sum(any(x[0]=='t'for x in t)for t in T))
