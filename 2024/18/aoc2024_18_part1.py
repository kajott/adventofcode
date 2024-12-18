R=[*range(-1,72)]
W={x+y*1j for x,y in[map(int,l.split(','))for l in open("input.txt")][:1024]}|{p for i in R for j in(-1,71)for p in(i+j*1j,i*1j+j)}
t,q,v=0,{0},{0}
while(70+70j in v)-1:t+=1;q={p+d for p in q for d in(-1,1,-1j,1j)}-W-v;v|=q
print(t)
