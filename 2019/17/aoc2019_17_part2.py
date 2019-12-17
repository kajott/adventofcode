from collections import*
_,E,L=int,enumerate,len
M=defaultdict(_,E(map(_,open("input.txt").read().split(','))));p=s=0;M[0]=2
def R(I):
 global p,s;q=[]
 while M[p]!=99:
  o=M[p];l=map(_,str(o)[-3::-1]+"000");o%=100;n=_("0331122331"[o]);i,j,k=[M[p+x]+s*(m>1)for x,m in zip((1,2,3),l)];a,b=[(M[x]if m-1else x)for x,m in zip((i,j),l)];p+=n+1
  if o<2:M[k]=a+b
  elif o<3:M[k]=a*b
  elif o<4:
   if I:M[i]=I.pop(0)
   else:p-=2;break
  elif o<5:q+=[a]
  elif o>8:s+=a
  elif o>7:M[k]=a==b
  elif o>6:M[k]=a<b
  elif(o>5)^(a!=0):p=b
 return q
G={99}
for y,l in E(''.join(map(chr,R([]))).split('\n')):
 for x,c in E(l):
  z=x+y*1j
  if'.'>c:G|={z}
  if'^'==c:r=z;d=-1j
P=[];w=0
while 1:
 if r+d in G:w+=1;r+=d
 else:
  if w:P+=[t+str(w)];w=0
  if r+d*1j in G:t="R,";d*=1j
  elif r-d*1j in G:t="L,";d*=-1j
  else:break
def C(d,r,F):
 n=L(F);z=r==[]and n<4and(d,F)
 if L(d)>9or z:return z
 for i,f in E(F):
  if f==r[:L(f)]:z=z or C(d+[i],r[L(f):],F)
 for l in(2,3,4,5):
  if n<3and L(','.join(r[:l]))<21:z=z or C(d+[n],r[l:],F+[r[:l]])
 return z
P,F=C([],P,[])
print R(map(ord,'\n'.join([','.join("ABC"[f]for f in P)]+[','.join(f)for f in F]+['n\n'])))[-1]
