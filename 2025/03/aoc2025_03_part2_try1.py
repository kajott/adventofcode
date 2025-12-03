r=0
for l in open("input.txt"):
 m,n="",l.strip()
 for e in range(-11,1):x,s=max((n[j],-j)for j in range(len(n)+e));m+=x;n=n[1-s:]
 r+=int(m)
print(r)
