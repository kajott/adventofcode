R=[*range(-1,72)];W={p for i in R for j in(-1,71)for p in(i+j*1j,i*1j+j)}
for x,y in(map(int,l.split(','))for l in open("input.txt")):
 W|={x+y*1j};q,v={0},{0}
 while q:q={p+d for p in q for d in(-1,1,-1j,1j)}-W-v;v|=q
 if(70+70j in v)-1:break
print(f"{x},{y}")
