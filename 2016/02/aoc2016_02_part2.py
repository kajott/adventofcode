T,p,r={'U':"121452349678B",'D':"36785ABC9ADCD",'L':"122355678AABD",'R':"134467899BCCD"},"5",""
for l in open("input.txt"):
 for c in l.strip():p=T[c][int(p,16)-1]
 r+=p
print r
