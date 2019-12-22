N=119315717514047
P=101741582076661
def G(a,b):
 if a<1:return(b,0,1)
 g,x,y=G(b%a,a);return(g,y-(b/a)*x,x)
I=lambda x:G(x,N)[1]%N
m,a,s,c=1,0,1,0
for l in list(open("input.txt"))[::-1]:
 w=l.split()
 if'c'==l[0]:a+=int(w[-1])
 elif'w'==l[5]:n=I(int(w[-1]));m,a=m*n,a*n
 else:n=I(N-1);m,a=m*n,(a+1)*n
print m%N,a%N
while P:
 if P&1:s,c=m*s,m*c+a
 P>>=1;m,a=m*m%N,m*a+a
print(2020*s+c)%N
