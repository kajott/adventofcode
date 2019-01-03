import re
a,b=map(int,re.findall('\d+',open("input.txt").read()))
n,m=0,2**31-1
for x in xrange(5*10**6):
 c,d=1,1
 while c:a=a*16807%m;c=a&3
 while d:b=b*48271%m;d=b&7
 n+=(a^b)&65535<1
print n
