f=open("input.txt");I=f.readline().strip();L=len(I)
N={n:(a,b)for n,a,b in(l.translate(str.maketrans("","","(=),")).split()for l in f if'@'<l)}
t,p=0,"AAA"
while"ZZZ">p:p=N[p][I[t%L]>'L'];t+=1
print(t)
