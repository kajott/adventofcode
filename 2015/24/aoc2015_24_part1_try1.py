N=map(int,open("input.txt"))[::-1]
R=range(len(N))
S=sum(N)/3
l=99
for i in xrange(1,1<<len(N)):
 s=[N[j]for j in R if(i>>j)&1]
 t=len(s)
 if sum(s)==S and t<=l:
  if t<l:l=t;q=1e99
  x=reduce(lambda a,b:a*b,s)
  if x<q:q=x;print q
