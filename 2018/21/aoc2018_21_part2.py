import re
n=sorted(set(map(int,re.findall('\d+',open("input.txt").read()))))[-2]
b,s=0,{-1}
while not s&{b}:
 s|={b};a,b,p=b|65536,n,b
 for i in(0,8,16):b=((b+(a>>i)%256)*65899)&0xFFFFFF
print p
