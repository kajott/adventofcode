M=dict(x.strip().split(')')[::-1]for x in open("input.txt"))
O=lambda k:k in M and O(M[k])+1
print sum(map(O,M))
