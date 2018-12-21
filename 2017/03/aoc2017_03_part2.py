N=361527
p=[19*[0]for x in range(19)]
x,y,h,v,r,d,i=9,9,1,0,1,1,0
p[y][x]=1
while i<=N:
 x+=h;y+=v;r-=1
 if r<1:
  if v:d+=1
  h,v,r=v,-h,d
 i=sum(sum(r[x-1:x+2])for r in p[y-1:y+2])
 p[y][x]=i
print i
