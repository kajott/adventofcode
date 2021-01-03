_,N=range,1000000
A=map(int,"463528179")+_(10,N+1)
M=[0]*(N+1);p=A[0]
for i in _(N):M[A[i-1]]=A[i]
for t in _(10*N):
 a=M[p];b=M[a];c=M[b];n=M[c];r={a,b,c,p};d=p
 while d in r:d=(d-1)if d>1else N
 M[c]=M[d];M[d]=a;M[p]=n;p=n
print M[1]*M[M[1]]
