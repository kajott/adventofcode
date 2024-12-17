import re;P=[*map(int,re.findall(r'\d+',open("input.txt").read()))][3:];L=len(P)
def R(a):
 *r,i=[a]+[0]*4
 while i<L:
  o,p=P[i:i+2];a,b,c=r[:3];i=p if(o==3)*a else i+2
  if(229>>o&1)*(p>3):p=r[p-4]
  if o==5:yield p&7
  d=a>>p;r[40404>>(2*o)&3]=[d,b^p,p&7,0,b^c,0,d,d][o]
C=lambda a,i:min([C(x,i-1)for x in range(max(1,8*a),8*a+8)if[*R(x)]==P[i-1:]],default=1e99)if i else a
print(C(0,L))
