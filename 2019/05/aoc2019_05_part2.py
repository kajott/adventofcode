M,p=map(int,open("input.txt").read().split(',')),0
while M[p]!=99:
 o,i,j,k=M[p:p+4];l=map(int,str(o)[-3::-1]+"00");o%=100;n=int("033112233"[o]);l[n:]=[1];a,b=[(x if l else M[x])for x,l in zip((i,j),l)];p+=n+1
 if o<2:M[k]=a+b
 elif o<3:M[k]=a*b
 elif o<4:M[i]=5
 elif o<5:R=a
 elif o>7:M[k]=a==b
 elif o>6:M[k]=a<b
 elif(o>5)^(a!=0):p=b
print R
