import operator as O
V,F,R,H={},{},"root","humn"
for l in open("input.txt"):
 l=l.split()
 if len(l)<3:V[l[0][:4]]=int(l[1])
 else:F[l[0][:4]]=l[1:]
E=lambda n:V[n]if(n in V)else{'+':O.add,'-':O.sub,'*':O.mul,'/':O.div}[F[n][1]](E(F[n][0]),E(F[n][2]))
F[R][1]='-';V[H]=0;a=E(R);V[H]=1E15
print int(a*1E15*1./(a-E(R)))
