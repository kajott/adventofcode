E="012=-"
s=0;r=""
for l in open("input.txt"):
 n=0
 for c in l.strip():n=n*5+{E[d]:d for d in range(-2,3)}[c]
 s+=n
while s:d=s%5;c=d>2;d-=5*c;r=E[d]+r;s=s/5+c
print r
