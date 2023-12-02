A,S=0,str.split
for l in open("input.txt"):
 _,l=l.split(':');m={}
 for g in S(l,';'):
  for c in S(g,','):n,c=S(c);m[c[0]]=max(m.get(c[0],0),int(n))
 A+=m['r']*m['g']*m['b']
print(A)
