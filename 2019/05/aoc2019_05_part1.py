M,p=map(int,open("input.txt").read().split(',')),0
while M[p]!=99:
 o,i,j,k=M[p:p+4];l=map(int,str(o)[-3::-1]+"00");o%=100;n=1+2*(o<3);l[n:]=[1];a,b=[(x if l else M[x])for x,l in zip((i,j),l)];p+=n+1
 if o<2:M[k]=a+b
 elif o<3:M[k]=a*b
 elif o<4:M[i]=1
 else:R=a
print R
