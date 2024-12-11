E=enumerate;M=F,U=[[],[]];p=c=0
for i,s in E(map(int,open("input.txt").read().strip())):M[i&1]+=[[p,s]];p+=s
while F:
 p,s=F.pop();e=[i for i,(z,q)in E(U)if(q>=s)*(z<p)]
 if e:e=U[e[0]];p=e[0];e[0]+=s;e[1]-=s
 c+=len(F)*(p*s+s*(s-1)//2)
print(c)
