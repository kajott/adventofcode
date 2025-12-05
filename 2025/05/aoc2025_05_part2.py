E=[];s=c=d=0
for L in open("input.txt"):
 if'-'in L:a,b=map(int,L.split('-'));E+=[(a,1),(b+1,-1)]
for x,i in sorted(E):c+=(d>0)*(x-s);d+=i;s=x
print(c)
