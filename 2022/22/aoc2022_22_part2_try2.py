import re
R,E,M=range,enumerate,[]
for y,I in E(open("input.txt")):M+=[(y+1,x+1,c)for x,c in E(I)if' '<c]
p,f=M[0][0]*1j+M[0][1],0
M={y*1j+x:c>'#'for y,x,c in M}
D=lambda i:int('g05nrdd23qwpbe5u8y95llxt3bts3dvl',36)>>i&3
C=lambda b:D(b)*50+D(b+2)*49+1
T=lambda b,n,x:(C(b)+C(b+4)*1j+n*1j**D(b+8),D(b+10)^x)
P={T(b+d,n,0):T(b+12-d,n,2)for n in R(50)for d in(0,12)for b in R(0,168,24)}
for n in re.findall('\d+|\w',I):
 if'@'<n:f=f+(n>'L')*2-1&3
 else:
  for i in R(int(n)):
   n,g=P.get((p,f),(p+1j**f,f))
   if M[n]:p,f=n,g
print int(p.imag*250+p.real)*4+f
