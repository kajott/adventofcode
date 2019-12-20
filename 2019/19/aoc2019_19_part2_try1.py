O=map(int,open("input.txt").read().split(','))
def S(x,y):
 M=dict(enumerate(O));p=s=0
 while 1:
  o=M[p];l=map(int,str(o)[-3::-1]+"000");o%=100;n=int("0331122331"[o]);i,j,k=[M.get(p+u,0)+s*(m>1)for u,m in zip((1,2,3),l)];a,b=[(M.get(u,0)if m-1else u)for u,m in zip((i,j),l)];p+=n+1
  if o<2:M[k]=a+b
  elif o<3:M[k]=a*b
  elif o<4:M[i]=x;x=y
  elif o<5:return a
  elif o>8:s+=a
  elif o>7:M[k]=a==b
  elif o>6:M[k]=a<b
  elif(o>5)^(a!=0):p=b
s,u=99,1;v=x=0
while s:
 x+=s;v=v*x/u;u=x
 while S(u,v)-1:v+=1
 y=v*S(x-99,v+99)
 if y:x-=s;s/=99
print(x-98)*10000+y
