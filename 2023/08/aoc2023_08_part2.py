f=open("input.txt");I=f.readline().strip();L=len(I);A=L
N={n:(a,b)for n,a,b in(l.translate(str.maketrans("","","(=),")).split()for l in f if'@'<l)}
for p in N:
 if'B'>p[2]:
  t=0
  while'Z'>p[2]:p=N[p][I[t%L]>'L'];t+=1
  A*=t//L
print(A)
