def F(x):
 x,y=x.real,x.imag;r,f=1,int(x*(x+3+2*y)+y+y*y+1362)
 while f:r^=f&1;f>>=1
 return(min(x,y)>=0)*r
x=1+1j;d,p,q,a=0,{x},set(),{x}
while d<51:
 x=p.pop();a|={x};q|={n for n in(x+1,x-1,x+1j,x-1j)if F(n)}-a
 if not p:p=q;q=set();d+=1
print len(a)
