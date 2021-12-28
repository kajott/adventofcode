L=map(len,''.join(l.split('|')[1]for l in open("input.txt")).split())
S=lambda n:L.count(n)
print S(2)+S(3)+S(4)+S(7)
