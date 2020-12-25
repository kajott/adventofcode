p,d=0,10+1j
for l in open("input.txt"):o=l[0];n=int(l[1:]);d+={"N":1j,"S":-1j,"W":-1,"E":1}.get(o,0)*n;d*={"L":1j,"R":-1j}.get(o,1)**(n/90);p+=(o=="F")*d*n
print int(abs(p.real)+abs(p.imag))
