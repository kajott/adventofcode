p,V=0,[{0},{0},{0}]
for l in open("input.txt"):
 d,n,_=l.split();n=int(n);d={'L':-1,'R':1,'U':1j,'D':-1j}[d]
 for f in(-1,0,1):V[f]|={p+i*d+f*1j*d for i in range(n)}
 p+=n*d
L=V[0];M=int(max(p.real for p in L))+1
for f in(1,-1):
 t=e=V[f]-L
 while e and(M in e)-1:t|=e;e={p+d for p in e for d in(1,-1,1j,-1j)}-L-t
 if not e:print(len(t|L))
