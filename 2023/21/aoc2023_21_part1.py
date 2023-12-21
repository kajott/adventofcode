R,E=set(),enumerate
for y,l in E(open("input.txt")):
 for x,c in E(l):
  p=y*1j+x
  if'.'>c:R|={p}
  if'A'<c:q={p}
for t in range(64):q={p+d for p in q for d in(1,-1,1j,-1j)}-R
print(len(q))
