M,s=2**24-1,0
for x in map(int,open("input.txt")):
 for _ in range(2000):x^=x<<6;x&=M;x^=x>>5;x^=x<<11
 s+=x&M
print(s)
