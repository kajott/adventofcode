import operator as O
V,F,n={},{},"root"
for l in open("input.txt"):
 l=l.split()
 if len(l)<3:V[l[0][:4]]=int(l[1])
 else:F[l[0][:4]]=l[1:]
E=lambda n:V[n]if(n in V)else{'+':O.add,'-':O.sub,'*':O.mul,'/':O.floordiv}[F[n][1]](E(F[n][0]),E(F[n][2]))
print(E(n))
S=lambda n:n=="humn"or(n in F)and(S(F[n][0])!=0)-(S(F[n][2])!=0)
while"humn"!=n:s,f=S(n),F[n];o,v,p,n=f[1],E(f[1+s]),n,f[1-s];t=v if"root"==p else t//v if'+'>o else t-v if','>o else(0,t+v,v-t)[s]if'.'>o else(0,t*v,v//t)[s]
print(t)
