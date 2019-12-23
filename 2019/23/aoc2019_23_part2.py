N=[dict(enumerate([[],[i],0,0]+map(int,open("input.txt").read().split(',')),-4))for i in range(50)]
u=v=w=c=0;l=1
while c!=l:
 for _ in N:
  while len(_[-4])<3:
   o=_[_[-1]];l=map(int,str(o)[-3::-1]+"000");o%=100;n=int("0331122331"[o]);i,j,k=[_.get(_[-1]+x,0)+_[-2]*(m>1)for x,m in zip((1,2,3),l)];a,b=[(_.get(x,0)if m-1else x)for x,m in zip((i,j),l)];_[-1]+=n+1
   if o<2:_[k]=a+b
   elif o<3:_[k]=a*b
   elif o<4:
    if _[-3]:_[i]=_[-3].pop(0)
    else:_[-1]-=2;_[-3]+=[-1];w+=1;break
   elif o<5:_[-4]+=[a]
   elif o>8:_[-2]+=a
   elif o>7:_[k]=a==b
   elif o>6:_[k]=a<b
   elif(o>5)^(a!=0):_[-1]=b
  if[]!=_[-4]:
   d,x,y=_[-4];_[-4]=[];w=0
   if d>49:u,v=x,y
   else:N[d][-3]+=[x,y]
 if(w>49)*v:l=c;c=v;w=0;N[0][-3]+=[u,v]
print c
