import re
G=filter(None,(map(int,re.findall('\d+',l))for l in open("input.txt")))
print sum((a!=b)*(a[3]<=b[4])for a in G for b in G if a[3])
