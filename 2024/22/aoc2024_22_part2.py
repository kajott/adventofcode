M,t,z=2**24-1,{},0
for x in map(int,open("input.txt")):
 a=b=c=d=l=x%10;v={}
 for _ in range(2000):
  x^=x<<6;x&=M;x^=x>>5;x^=x<<11;p=(x&M)%10;a,b,c,d=b,c,d,p-l;s,l=(a,b,c,d),p
  if(s in v)-1:v[s]=t[s]=t.get(s,0)+p
print(max(t.values()))
