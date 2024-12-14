import re;N=map(int,re.findall(r'\d+',open("input.txt").read()))
A,r=int(10**13),0
while N:k,t,u,v,x,y,*N=N;s,u,x=k*t,u*t,(x+A)*t;i,j=abs(u-v*k),abs(x-(y+A)*k);b=j//i;n=x-b*u;r+=(j%i+n%s<1)*(3*n//s+b)
print(r)
