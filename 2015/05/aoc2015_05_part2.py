import re
M=lambda r,l:bool(re.search(r,l))
print sum(M(r'(\w\w).*\1',l)*M(r'(\w)\w\1',l)for l in open("input.txt"))
