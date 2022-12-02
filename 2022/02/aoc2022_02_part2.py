S=0
for L in open("input.txt"):a,r=map(ord,L.split());a-=64;r-=87;S+=(a+r)%3+3*r-2
print S
