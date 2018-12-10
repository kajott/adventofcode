import re,collections as C
D=C.defaultdict
l,g,r=D(int),D(set),""
for a,b in (re.findall(r'\b\w\b',x) for x in open("input.txt")):g[a].add(b);l[a]+=0;l[b]+=1
while l:
 x=min((c,x) for x,c in l.items())[1]
 for y in g[x]:l[y]-=1
 r+=x;del l[x]
print r
