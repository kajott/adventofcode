import re;k=0
for l in open("input.txt"):
 if','in l:R="("+l.replace(',','|')+r")+\s*$"
 if re.match(R,l,re.X):k+=1
print(k)
