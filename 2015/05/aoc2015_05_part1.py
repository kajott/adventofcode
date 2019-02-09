import re
F=lambda r,l:len(re.findall(r,l))
print sum((F('ab|cd|pq|xy',l)<1)*(F(r'(\w)\1',l)>0)*(F('[aeiou]',l)>2)for l in open("input.txt"))
