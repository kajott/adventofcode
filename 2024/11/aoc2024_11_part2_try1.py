f={n:1 for n in open("input.txt").read().split()}
for t in range(75):
 p,f=f,{}
 for n in p:
  l=len(n);q=['1']if n<'1'else[str(int(n)*2024)]if l&1 else[n[:l//2],str(int(n[l//2:]))]
  for z in q:f[z]=f.get(z,0)+p[n]
print(sum(f.values()))
