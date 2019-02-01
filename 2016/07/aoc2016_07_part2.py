import re
R='\[.*?\]'
B=lambda x:{x[i:i+2]for i in range(len(x)-2)if x[i+2]==x[i]}
r=0
for a in open("input.txt"):h=B(''.join(re.findall(R,a)));r+=any((b+a in h)for a,b in B(re.sub(R,'[]',a))if a!=b)
print r
