import re
C,i=[[p]for p in(map(int,re.findall('-?\d+',l))for l in open("input.txt"))],0
while i<len(C):
 j,m=i+1,0
 while j<len(C):
  if any(any(sum(abs(x-y)for x,y in zip(a,b))<4for b in C[j])for a in C[i]):C[i]+=C[j];del C[j];m+=1
  else:j+=1
 if m<1:i+=1
print len(C)
