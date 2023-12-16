A=0
for p in open("input.txt").read().strip().split(','):
 h=0
 for c in p:h=(h+ord(c))*17&255
 A+=h
print(A)
