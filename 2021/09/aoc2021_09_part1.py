E,M,Q=enumerate,{},lambda q:M.get(q,9)
for y,l in E(open("input.txt")):
 for x,i in E(l.strip()):M[x+1j*y]=int(i)
print sum(M[p]+1for p in M if M[p]<min(Q(p+1),Q(p-1),Q(p-1j),Q(p+1j)))
