R=range
M,t,f=[map(int,l[:10])+[0]for l in open("input.txt")],0,""
M+=[11*[0]]
while len(f)<100:
 M,f,s=[[x+1for x in r]for r in M],set(),1;t+=1
 while s:
  s={(x,y)for x in R(10)for y in R(10)if M[y][x]>9}-f;f|=s
  for x,y in s:
   for v in R(y-1,y+2):
    for u in R(x-1,x+2):M[v][u]+=1
 for x,y in f:M[y][x]=0
print t
