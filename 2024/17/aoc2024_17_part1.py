import re;R=[*map(int,re.findall(r'\d+',open("input.txt").read()))]
I,S,P=0,[],R[3:]
while I<len(P):
 o,p=P[I:I+2];a,b,c=R[:3];I=p if(o==3)*a else I+2
 if(229>>o&1)*(p>3):p=R[p-4]
 if o==5:S+=[p&7]
 d=a>>p;R[40404>>(2*o)&3]=[d,b^p,p&7,0,b^c,0,d,d][o]
print(','.join(map(str,S)))
