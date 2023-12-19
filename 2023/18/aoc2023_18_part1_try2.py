A=C=x=y=0
for l in open("input.txt"):d,n,_=l.split();n=int(n);u,v={'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)}[d];x,y,u,v=x+u*n,y+v*n,x,y;C+=n;A+=x*v-y*u
print((abs(A)+C)//2+1)
