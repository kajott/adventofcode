n=[[0]+[".|#".index(c)for c in r.strip()]+[0]for r in open("input.txt")]
w,h=len(n[0]),len(n)
n[:0]=[[0]*w];n+=[[0]*w]
for t in range(10):
 o=[r[:]for r in n]
 for y in range(1,h+1):
  for x in range(1,w-1):
   c=o[y][x];s=3*[0];s[c]-=1
   for v in range(y-1,y+2):
    for u in range(x-1,x+2):s[o[v][u]]+=1
   if c<1and s[1]>2:c=1
   elif c==1and s[2]>2:c=2
   elif c>1and s[1]*s[2]<1:c=0
   n[y][x]=c
C=lambda s:sum(sum(x==s for x in r)for r in n)
print C(1)*C(2)
