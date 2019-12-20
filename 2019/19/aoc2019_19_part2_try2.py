O=map(int,open("input.txt").read().split(','))
def S(x,y):
 M=dict(enumerate(O));p=s=0
 while 1:
  o=M[p];l=map(int,str(o)[-3::-1]+"000");o%=100;n=int("0331122331"[o]);i,j,k=[M.get(p+u,0)+s*(m>1)for u,m in zip((1,2,3),l)];a,b=[(M.get(u,0)if m-1else u)for u,m in zip((i,j),l)];p+=n+1
  if o<2:M[k]=a+b
  elif o<3:M[k]=a*b
  elif o<4:M[i]=x;x=y
  elif o<5:return 1-a
  elif o>8:s+=a
  elif o>7:M[k]=a==b
  elif o>6:M[k]=a<b
  elif(o>5)^(a!=0):p=b
x,y=99,0
while S(x-99,y+99):
 x+=1
 while S(x,y):y+=1
print(x-99)*10000+y
