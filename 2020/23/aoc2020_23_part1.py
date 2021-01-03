N=map(int,"463528179")
for t in range(100):
 c=N[:1];r=N[1:4];del N[:4];d=c[0]-1
 while not d in N:d=d-1if d>1else 9
 d=N.index(d)+1;N[d:d]=r;N+=c
p=N.index(1);print''.join(map(str,N[p+1:]+N[:p]))
