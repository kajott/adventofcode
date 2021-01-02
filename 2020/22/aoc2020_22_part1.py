A,B=[],[]
for l in map(str.strip,open("input.txt")):
 if"P"==l[:1]:A,B=B,A
 elif l:B+=[int(l)]
while A and B:
 a=A.pop(0);b=B.pop(0)
 if a>b:A+=[a,b]
 else:B+=[b,a]
print sum(c*(i+1)for i,c in enumerate((A+B)[::-1]))
