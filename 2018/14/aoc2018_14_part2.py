N="640441"
r,p,f="37",[0,1],-1
while f<0:
 s=ord(r[p[0]])+ord(r[p[1]])-96
 if s>9:r+='1'
 r+=str(s%10);l=len(r);p=[(x+ord(r[x])-47)%l for x in p];f=r.find(N,l-len(N)-2)
print f
