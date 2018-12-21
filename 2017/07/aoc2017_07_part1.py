import re
e,r={0},{0}
for x in open("input.txt"):
 w=re.findall('[a-z]+',x);e|={w[0]}
 for q in w[1:]:r|={q}
print list(e-r)[0]
