import re,heapq as H
def A(z):H.heappush(q,z)
def C(m):global t;t=b[:];t[0]+=m;t[3]-=m;return t[3]>=0
i,D=map(int,re.findall('\d+',open("input.txt").read()))
s=[0,i,50,500]+4*[0];q=[s]
while s[1]>0:
 s=H.heappop(q);b=s[:];b[4]^=1;a=(b[5]>0)*7
 if b[2]<=0:continue
 if a:b[5]-=1
 if b[6]:b[6]-=1;b[1]-=3
 if b[7]:b[7]-=1;b[3]+=101
 if b[1]<=0:A(b)
 if s[4]:b[2]-=max(1,D-a);A(b);continue
 if C(53):t[1]-=4;A(t)
 if C(73):t[1]-=2;t[2]+=2;A(t)
 for m,i,d in((113,5,6),(173,6,6),(229,7,5)):
  if C(m)and t[i]<1:t[i]=d;A(t)
print s[0]
