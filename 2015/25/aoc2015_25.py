import re
y,x=map(int,re.findall('\d+',open("input.txt").read()))
d=x+y-2;n=20151125
for i in range((d*d+d)/2+x-1):n=(n*252533)%33554393
print n
