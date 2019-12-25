import re
_=map
B="north east west south loo pho lav mag esc".split()
N,E,W,S=B[:4];D=set(B[:4]);B=B[4:]
Z={N:S,S:N,E:W,W:E,"":""}
M=dict(enumerate(_(int,open("input.txt").read().split(','))));p=s=0
def R(c):
 global p,s;I=_(ord,c)+[10];O=[]
 while M[p]!=99:
  o=M[p];l=_(int,str(o)[-3::-1]+"000");o%=100;n=int("0331122331"[o]);i,j,k=[M.get(p+x,0)+s*(m>1)for x,m in zip((1,2,3),l)];a,b=[(M.get(x,0)if m-1else x)for x,m in zip((i,j),l)];p+=n+1
  if o<2:M[k]=a+b
  elif o<3:M[k]=a*b
  elif o<4:
   if I:M[i]=I.pop(0)
   else:p-=2;break
  elif o<5:O+=[a]
  elif o>8:s+=a
  elif o>7:M[k]=a==b
  elif o>6:M[k]=a<b
  elif(o>5)^(a!=0):p=b
 return''.join(_(chr,O))
I=[]
def V(p,g):
 global P,F,I;p=p+[g];t=R(g);o=set(re.findall('^- (.*)$',t,re.M));d=(o&D)-{Z[g]};I+=[i for i in o-D if not any(b in i for b in B)and R("take "+i)]
 if"Che"in t:P=p;F=d.pop()
 else:[V(p,d)for d in d]
 if g:R(Z[g])
V([],"")
[R(d)for d in P]
h=set(I);n=len(I)
for c in range(1<<n):
 w={I[b]for b in range(n)if(c>>b)&1};[R("drop "+i)for i in h-w];[R("take "+i)for i in w-h];h=w;a=filter(str.isdigit,R(F).split())
 if a:break
print a[0]
