N=345
p,l,z=1,1,0
while l<50000000:
 l+=1;p=(p+N+1)%l;z+=(z>=p)
 if(z+1)%l==p:a=l
print a
