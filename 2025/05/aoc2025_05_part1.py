R,F=[],open("input.txt")
for L in F:
 if"0">L:break
 R+=[[*map(int,L.split('-'))]]
print(sum(any(a<=int(L)<=b for a,b in R)for L in F))
