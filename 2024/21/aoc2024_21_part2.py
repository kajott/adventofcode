E=enumerate
M=lambda k:{c:x+y*1j for y,r in E(k.split())for x,c in E(r)};M=[M("789 456 123 x0A"),M("x^A <v>")]
import functools as F
@F.cache
def D(s,n):
 if n>25:return len(s)
 m=M[n>0];c,i,r=m['A'],m['x'],0
 for k in s:
  u=m[k];q,z=[(c,'')],[]
  while q:
   x,p=q.pop()
   if x==u:z+=[p+'A']
   elif x-i:q+=[(x+a,p+d)for a,d in((-1,'<'),(1,'>'),(-1j,'^'),(1j,'v'))if((x-u)*a.conjugate()).real<0]
  r+=min(D(p,n+1)for p in z);c=u
 return r
print(sum(D(s:=l.strip(),0)*int(s[:-1])for l in open("input.txt")))
