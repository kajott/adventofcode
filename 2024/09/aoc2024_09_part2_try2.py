import heapq as H;P=H.heappush
E=enumerate;F=[];U={};p=c=0
for i,s in E(map(int,open("input.txt").read().strip())):
 if i&1:U[s]=U.get(s,[]);P(U[s],p)
 else:F+=[(p,s)]
 p+=s
while F:
 p,s=F.pop();e=[(U[q][0],q)for q in U if U[q]and(q>=s)*(U[q][0]<p)]
 if e:p,q=min(e);H.heappop(U[q]);P(U[q-s],p+s)
 c+=len(F)*(p*s+s*(s-1)//2)
print(c)
