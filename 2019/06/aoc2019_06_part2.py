M=dict(x.strip().split(')')[::-1]for x in open("input.txt"))
P=lambda k:k in M and[k]+P(M[k])or[]
a,b=P("YOU"),P("SAN")
while a.pop()==b.pop():0
print len(a)+len(b)
