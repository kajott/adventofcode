n=map(int,open("input.txt"))
for a in n:
 for b in n:
  for c in n:
   if a+b+c==2020:print a*b*c
