S,R=0,[set(L.strip())for L in open("input.txt")]
while R:c=ord((R[0]&R[1]&R[2]).pop());S+=min(c-38,(c-96)%99);del R[:3]
print S
