b,h,s,a=map(int,open("input.txt").read().strip().split()),{0},0,0
while 1:
 t=tuple(b)
 if t in h:
  if a:break
  a-=1;s=0;h={0}
 h|={t};s+=1
 m,i=min((-x,i)for i,x in enumerate(b))
 b[i]=0
 while m:i=(i+1)%len(b);b[i]+=1;m+=1
print s
