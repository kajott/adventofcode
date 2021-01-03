import re
class N:
 def __init__(_,n):_.n=n
 def __add__(a,b):return N(a.n*b.n)
 def __mul__(a,b):return N(a.n+b.n)
R=str.replace
print sum(eval(R(R(R(re.sub('(\d+)',r'N(\1)',x),'+','#'),'*','+'),'#','*')).n for x in open("input.txt"))
