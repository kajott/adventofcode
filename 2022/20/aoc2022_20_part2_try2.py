class V:pass
F,i,L=0,V(),[]
for n in open("input.txt"):i.n=V();i=i.n;i.v=int(n)*811589153;F=F or i;L+=[i]
i.n=0
for r in range(10):
 x=F
 while x:i=L.index(x);del L[i];L.insert((i+x.v)%len(L),x);x=x.n
L=[x.v for x in L];print(sum(L[(L.index(0)+i*1000)%len(L)]for i in(1,2,3)))
