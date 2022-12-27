import re
E,M=enumerate,[]
for y,I in E(open("input.txt")):M+=[(y+1,x+1,c)for x,c in E(I)if' '<c]
p,f,d=M[0][0]*1j+M[0][1],0,1
M={y*1j+x:c>'#'for y,x,c in M}
for n in re.findall('\d+|\w',I):
 if'@'<n:f+=(n>'L')*2-1;d=1j**f
 else:
  for i in range(int(n)):
   n=p+d
   if(n in M)-1:
    while n-d in M:n-=d
   if M[n]:p=n
print int(p.imag*250+p.real)*4+f%4
