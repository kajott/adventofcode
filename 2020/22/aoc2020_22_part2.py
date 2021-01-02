A,B=[],[]
for l in map(str.strip,open("input.txt")):
 if"P"==l[:1]:A,B=B,A
 elif l:B+=[int(l)]
def G(A,B):
 v={0}
 while A and B:
  s=tuple(A+[0]+B)
  if s in v:B=[];break
  v|={s};a=A.pop(0);b=B.pop(0)
  if b>a if a>len(A)or b>len(B)else G(A[:a],B[:b])[0]:B+=[b,a]
  else:A+=[a,b]
 return A<[0],sum(c*(i+1)for i,c in enumerate((A+B)[::-1]))
print G(A,B)[1]
