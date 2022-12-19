import re
E,M,A=(0,1,2,3),max,1
for l in list(open("input.txt"))[:3]:
 n,a,b,c,d,e,f=map(int,re.findall('\d+',l));B=((a,0,0,0),(b,0,0,0),(c,d,0,0),(e,0,f,0));R=(M(a,b,c,e),d,f,99);Q,V,G={(1,0,0,0,0,0,0,0,32)},{0},0
 while Q:
  q=Q-V;V|=q;Q=set()
  for s in q:
   t=s[8];g=s[7]+s[3]*t;G=M(G,g)
   for i in E:z=zip(B[i],s[4:],s);x=M(0,M(((n-h)+r-1)/r if r else(n-h)*99for n,h,r in z))+1;Q|=(t*t+t+1)/2+g>G and x<t and s[i]<R[i]and{tuple([s[j]+(j==i)for j in E]+[h+x*r-n for n,h,r in z]+[t-x])}or{0}
 A*=G
print A
