import re
R,M=range,{}
N=map(int,re.findall('\d+',open("input.txt").read()))
for x,y,u,v in[N[i:i+4]for i in R(0,len(N),4)]:
 i=j=1
 if((x-u)*(y-v))==0:
  while i|j:M[(x,y)]=M.get((x,y),0)+1;i=-1if x>u else x<u;x+=i;j=-1if y>v else y<v;y+=j
print sum(c>1for c in M.values())
