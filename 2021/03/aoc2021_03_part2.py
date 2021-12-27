N=[int(l,2)for l in open("input.txt")]
def R(c):
 b,n=2048,N
 while len(n)>1:m=((sum(x&b for x in n)*2>=b*len(n))^c)*b;n=[x for x in n if(x&b)==m];b/=2
 return n[0]
print R(1)*R(0)
