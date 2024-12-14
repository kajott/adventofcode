import re;N=map(int,re.findall(r'\d+',open("input.txt").read()))
R,r=[*range(101)],0
while N:s,t,u,v,x,y,*N=N;r+=sum((3*a+b)*(s*a+u*b==x)*(t*a+v*b==y)for a in R for b in R)
print(r)
