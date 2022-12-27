import re
E,M,P=enumerate,[],{}
for y,I in E(open("input.txt")):M+=[(y+1,x+1,c)for x,c in E(I)if' '<c]
p,f=M[0][0]*1j+M[0][1],0
M={y*1j+x:c>'#'for y,x,c in M}
C=lambda z:z in M
for s in M:
 for a in(0,1,2,3):
  b=a+1&3;u,v=1j**a,1j**b;l,r=s+u,s+v;c=2-C(s+u)*C(s+v)*(1-C(s+u+v))
  while c<2:
   P[(l,a+1&3)]=(r,b+1&3);P[(r,b-1&3)]=(l,a-1&3);l+=u;r+=v;c=0
   if C(l+1j**(a+1))+C(r+1j**(b-1)):c=2
   if C(l)-1:l-=u;a=a-1&3;u=1j**a;c+=1
   if C(r)-1:r-=v;b=b+1&3;v=1j**b;c+=1
for n in re.findall('\d+|\w',I):
 if'@'<n:f=f+(n>'L')*2-1&3
 else:
  for i in range(int(n)):
   n,g=P.get((p,f),(p+1j**f,f))
   if M[n]:p,f=n,g
print int(p.imag*250+p.real)*4+f
