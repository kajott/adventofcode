D,S,T={},[[],7],tuple
for L in open("input.txt"):
 t=L.split()
 if len(t)>2:S=S+[S[-1]+[t[2]]]if'/'<t[2]else S[:-1]
 if'0'<L<'@':
  for p in S:D[T(p)]=D.get(T(p),0)+int(t[0])
V=D.values()
print sum(s*(s<=1e5)for s in V)
print min(s for s in V if s>=D[T()]-4e7)
