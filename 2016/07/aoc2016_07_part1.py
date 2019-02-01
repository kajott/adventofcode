import re
F=re.findall
A=lambda x:any(a!=b for a,b in F(r'(\w)(\w)\2\1',x))
print sum(any(map(A,F('\[.*?\]',a)))^1*A(a)for a in open("input.txt"))
