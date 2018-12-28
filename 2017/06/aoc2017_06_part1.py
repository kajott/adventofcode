b,s,h=map(int,open("input.txt").read().strip().split()),0,{0}
while not tuple(b)in h:
 h|={tuple(b)};s+=1
 m,i=min((-x,i)for i,x in enumerate(b))
 b[i]=0
 while m:i=(i+1)%len(b);b[i]+=1;m+=1
print s
