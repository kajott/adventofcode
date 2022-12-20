E,R=enumerate,range
L=[(i,n*811589153)for i,n in E(map(int,open("input.txt")))];N=len(L)
for r in R(10):
 for i in R(N):p,d=min((j,x)for j,x in E(L)if x[0]==i);del L[p];L.insert((p+d[1])%(N-1),d)
L=[x[1]for x in L];print sum(L[(L.index(0)+i*1000)%N]for i in(1,2,3))
