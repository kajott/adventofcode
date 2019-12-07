from itertools import*
Z=map
class A:
 def __init__(_,i):_.M,_.p,_.q=Z(int,open("input.txt").read().split(','))+[0],0,[i]
 def r(_):
  while _.M[_.p]!=99:
   o,i,j,k=_.M[_.p:_.p+4];l=Z(int,str(o)[-3::-1]+"00");o%=100;n=int("033112233"[o]);l[n:]=[1];a,b=[(x if l else _.M[x])for x,l in zip((i,j),l)];_.p+=n+1
   if o<2:_.M[k]=a+b
   elif o<3:_.M[k]=a*b
   elif o<4:_.M[i]=_.q.pop(0)
   elif o<5:return a
   elif o>7:_.M[k]=a==b
   elif o>6:_.M[k]=a<b
   elif(o>5)^(a!=0):_.p=b
def S(s):
 m,r=Z(A,s),0
 for a in cycle(m):
  x=r;a.q+=[x];r=a.r()
  if r<1:return x
print max(Z(S,permutations(range(5,10))))
