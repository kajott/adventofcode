S=0
for L in open("input.txt"):L=L.strip();n=len(L)/2;c=ord((set(L[:n])&set(L[n:])).pop());S+=min(c-38,(c-96)%99)
print S
