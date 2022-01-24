from heapq import*
P,R,E,T,L=[0,1,3,5,7,9,10],[2,4,6,8],range,tuple,list
s=[int(c,16)-10for c in open("input.txt").read()if'@'<c]
s=[0]*4+[4]*4+s[4:]+[3,1,0,2,3,2,1,0]+s[:4]+[-1]*7
for i in E(4):
 while s[i+8]==i:s[i]+=1;s[i+4]-=1;s[i+8:i+24:4]=s[i+12:i+24:4]+[-1]
def F(a,b):a,b=sorted((a,b));return 1-any(s[i+24]>=0for i in E(7)if a<P[i]<b)
O=[(0,T(s))];C={T(s):0}
while O:
 c,s=heappop(O);m=[]
 if c>C.get(s,1e9):continue
 if min(s[:4])>3:break
 for i in E(7):
  r=s[i+24]
  if(r>=0)*(s[r+4]<1)*F(P[i],R[r]):d=L(s);d[i+24]=-1;d[r]+=1;m+=[(c+10**r*(abs(P[i]-R[r])+4-s[r]),T(d))]
 for i in E(4):
  if s[i+4]:
   k=i+s[i+4]*4+4;r=s[k];u=4-s[i]-s[i+4]+1;a=b=P.index(R[i]+1)
   while(s[a+23]<0)*a:a-=1
   while b<7and s[b+24]<0:b+=1
   for j in E(a,b):d=L(s);d[k]=-1;d[i+4]-=1;d[j+24]=r;m+=[(c+10**r*(abs(R[i]-P[j])+u),T(d))]
   if(s[r+4]<1)*F(R[i],R[r]):d=L(s);d[k]=-1;d[i+4]-=1;d[r]+=1;m+=[(c+10**r*(abs(R[i]-R[r])+u+4-s[r]),T(d))]
 for c,s in m:
  if c<C.get(s,1e9):C[s]=c;heappush(O,(c,s))
print c
