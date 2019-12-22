C=2019
N=10007
for l in open("input.txt"):
 w=l.split()
 if'c'==l[0]:C=(C+N-int(w[-1]))%N
 elif'w'==l[5]:C=(C*int(w[-1]))%N
 else:C=N-1-C
print C
