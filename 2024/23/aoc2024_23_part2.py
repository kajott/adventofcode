C,G={},{}
for l in open("input.txt"):a,b=map(str.strip,l.split('-'));C[a]=C.get(a,{b})|{b};C[b]=C.get(b,{a})|{a}
for a in C:
 g=[a]
 for b in C[a]:g+=[b]*all(b in C[c]for c in g)
 G[','.join(sorted(g))]=0
print(max((len(g),g)for g in G)[1])
