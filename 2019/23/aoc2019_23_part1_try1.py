class M:
 def __init__(_,i):_.m=dict(enumerate(map(int,open("input.txt").read().split(','))));_.p=_.s=0;_.i=[i];_.o=[]
N=map(M,range(50))
while N:
 for _ in N:
  while len(_.o)<3:
   o=_.m[_.p];l=map(int,str(o)[-3::-1]+"000");o%=100;n=int("0331122331"[o]);i,j,k=[_.m.get(_.p+x,0)+_.s*(m>1)for x,m in zip((1,2,3),l)];a,b=[(_.m.get(x,0)if m-1else x)for x,m in zip((i,j),l)];_.p+=n+1
   if o<2:_.m[k]=a+b
   elif o<3:_.m[k]=a*b
   elif o<4:
    if _.i:_.m[i]=_.i.pop(0)
    else:_.p-=2;_.i+=[-1];break
   elif o<5:_.o+=[a]
   elif o>8:_.s+=a
   elif o>7:_.m[k]=a==b
   elif o>6:_.m[k]=a<b
   elif(o>5)^(a!=0):_.p=b
  if[]!=_.o:
   d,x,y=_.o;_.o=[]
   if d>49:N=0;print y
   else:N[d].i+=[x,y]
