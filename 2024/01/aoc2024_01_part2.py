A,B=zip(*(map(int,l.split())for l in open("input.txt")))
print(sum(a*B.count(a)for a in A))
