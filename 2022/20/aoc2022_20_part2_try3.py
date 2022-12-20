V=[int(n)*811589153for n in open("input.txt")];N=len(V);O=range(N);I=O.index
for r in O*10:i=I(r);O.insert((i+V[O.pop(i)])%(N-1),r)
print sum(V[O[(I(V.index(0))+i*1000)%N]]for i in(1,2,3))
