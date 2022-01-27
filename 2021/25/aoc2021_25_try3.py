G,P,t=map(str.strip,open("input.txt")),0,0
X=lambda c:[''.join(r)for r in zip(*((r[-1]+r+r[0]).replace(c+'.','.'+c)[1:-1]for r in G))]
while P!=G:t+=1;P=G;G=X('>');G=X('v')
print t
