import re
S=0
for L in open("input.txt"):a,b,c,d=map(int,re.findall('\d+',L));S+=(c<=b)*(a<=d)
print S
