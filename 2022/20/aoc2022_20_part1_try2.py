class V:pass
x,i,L=0,V(),[]
for n in open("input.txt"):i.n=V();i=i.n;i.v=int(n);x=x or i;L+=[i]
i.n=0
while x:i=L.index(x);del L[i];L.insert((i+x.v)%len(L),x);x=x.n
L=[x.v for x in L];print(sum(L[(L.index(0)+i*1000)%len(L)]for i in(1,2,3)))
