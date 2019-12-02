for i in range(10000):
 M,p=map(int,open("input.txt").read().split(',')),0;M[1:3]=i/100,i%100
 while M[p]!=99:o,a,b,r=M[p:p+4];a,b=M[a],M[b];M[r]=a*b if o-1else a+b;p+=4
 if M[0]==19690720:print i
