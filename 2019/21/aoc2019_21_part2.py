M=dict(enumerate(map(int,open("input.txt").read().split(','))));p=s=0
I,R=map(ord,"OR B T\nAND C T\nNOT T J\nAND E T\nNOT T T\nAND T J\nAND D J\nAND H J\nNOT A T\nOR T J\nRUN\n"),0
while M[p]!=99:
 o=M[p];l=map(int,str(o)[-3::-1]+"000");o%=100;n=int("0331122331"[o]);i,j,k=[M.get(p+x,0)+s*(m>1)for x,m in zip((1,2,3),l)];a,b=[(M.get(x,0)if m-1else x)for x,m in zip((i,j),l)];p+=n+1
 if o<2:M[k]=a+b
 elif o<3:M[k]=a*b
 elif o<4:M[i]=I.pop(0)
 elif o<5:R=a
 elif o>8:s+=a
 elif o>7:M[k]=a==b
 elif o>6:M[k]=a<b
 elif(o>5)^(a!=0):p=b
print R
