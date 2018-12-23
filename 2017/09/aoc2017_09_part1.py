import re
l,s=0,0
for c in re.sub('<[^>]*>','',re.sub('!.','',open("input.txt").read().strip())):
 if c=='{':l+=1;s+=l
 elif c=='}':l-=1
print s
