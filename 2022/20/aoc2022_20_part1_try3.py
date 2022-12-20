V=map(int,open("input.txt"));N=len(V);O=range(N);I=O.index
for r in O*1:i=I(r);O.insert((i+V[O.pop(i)])%(N-1),r)
print sum(V[O[(I(V.index(0))+i*1000)%N]]for i in(1,2,3))
