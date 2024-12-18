R=[*range(-1,72)];W={p for i in R for j in(-1,71)for p in(i+j*1j,i*1j+j)}
N=[[*map(int,l.split(','))]for l in open("input.txt")]
a,b=0,len(N)
while a<b-1:
 c=(a+b)//2;q,v={0},W|{x+y*1j for x,y in N[:c]}
 while q:q={p+d for p in q for d in(-1,1,-1j,1j)}-v;v|=q
 if 70+70j in v:a=c
 else:b=c
x,y=N[a];print(f"{x},{y}")
