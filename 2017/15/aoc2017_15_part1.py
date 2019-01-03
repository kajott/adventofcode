import re
a,b=map(int,re.findall('\d+',open("input.txt").read()))
n,m=0,2**31-1
for x in xrange(4*10**7):a=a*16807%m;b=b*48271%m;n+=(a^b)&65535<1
print n
