q=z=0
M=dict(enumerate(map(int,open("input.txt").read().split(','))));p=s=0
while M[p]!=99:
 o=M[p];l=map(int,str(o)[-3::-1]+"000");o%=100;n=int("0331122331"[o]);i,j,k=[M.get(p+x,0)+s*(m>1)for x,m in zip((1,2,3),l)];a,b=[(M.get(x,0)if m-1else x)for x,m in zip((i,j),l)];p+=n+1
 if o<2:M[k]=a+b
 elif o<3:M[k]=a*b
 elif o<5:q=(q+1)%3;z+=q<1and a==2
 elif o>8:s+=a
 elif o>7:M[k]=a==b
 elif o>6:M[k]=a<b
 elif(o>5)^(a!=0):p=b
print z
