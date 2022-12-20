E=enumerate
L=list(E(map(int,open("input.txt"))));N=len(L)
for i in range(N):p,d=min((j,x)for j,x in E(L)if x[0]==i);del L[p];L.insert((p+d[1])%(N-1),d)
L=[x[1]for x in L];print sum(L[(L.index(0)+i*1000)%N]for i in(1,2,3))
