from collections import*
_=int;G=""
M=defaultdict(_,enumerate(map(_,open("input.txt").read().split(','))));p=s=0
while M[p]!=99:
 o=M[p];l=map(_,str(o)[-3::-1]+"000");o%=100;n=_("0331122331"[o]);i,j,k=[M[p+x]+s*(m>1)for x,m in zip((1,2,3),l)];a,b=[(M[x]if m-1else x)for x,m in zip((i,j),l)];p+=n+1
 if o<2:M[k]=a+b
 elif o<3:M[k]=a*b
 elif o<5:G+=chr(a)
 elif o>8:s+=a
 elif o>7:M[k]=a==b
 elif o>6:M[k]=a<b
 elif(o>5)^(a!=0):p=b
G=G.strip().split('\n')
print sum(x*y for x in range(1,len(G[0])-1)for y in range(1,len(G)-1)if"####.">G[y-1][x]+G[y][x-1:x+2]+G[y+1][x])
