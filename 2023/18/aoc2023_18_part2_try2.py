A=C=x=y=0
for l in open("input.txt"):l=l.split()[2];n=int(l[2:7],16);u=int(l[7]);u,v=u&1,1-(u&2);u,v=u*v-v,u*v;x,y,u,v=x+u*n,y+v*n,x,y;C+=n;A+=x*v-y*u
print((abs(A)+C)//2+1)
