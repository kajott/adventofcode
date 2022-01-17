S,P=''.join(format(int(x,16),'04b')for x in open("input.txt").read().strip()),[0]
def G(n):P[0]+=n;return int(S[P[0]-n:P[0]],2)
def D():
 v=G(3);t=G(3);x=-1
 if t==4:
  while x&16:x=G(5)
 elif G(1):
  for x in range(G(11)):v+=D()
 else:
  e=G(15);e+=P[0]
  while P[0]<e:v+=D()
 return v
print D()
