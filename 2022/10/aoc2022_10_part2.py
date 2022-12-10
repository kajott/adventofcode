v=3;P=[v]
for L in open("input.txt"):
 P+=[v]
 if'n'>L:v+=int(L.split()[1]);P+=[v]
for b in range(0,240,40):print''.join(" #"[P[i+b]-4<i<P[i+b]]for i in range(40))
