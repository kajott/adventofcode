S=0
for L in open("input.txt"):a,b=map(ord,L.split());a-=64;b-=87;S+=b+3*(a==b)+6*(a%3+1==b)
print S
