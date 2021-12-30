M=[map(int,l.strip())for l in open("input.txt")]
for y in range(len(M)):
 for x in range(len(M[y])):
  a=[]
  if x:a+=[M[y][x-1]]
  if y:a+=[M[y-1][x]]
  if a:M[y][x]+=min(a)
print M[-1][-1]-M[0][0]
