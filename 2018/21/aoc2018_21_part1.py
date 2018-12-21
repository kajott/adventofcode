import re
b=sorted(set(map(int,re.findall('\d+',open("input.txt").read()))))[-2]
for i in(0,0,1):b=((b+i)*65899)&0xFFFFFF
print b
