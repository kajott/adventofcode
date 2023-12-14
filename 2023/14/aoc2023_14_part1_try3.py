M=[''.join(c[::-1])for c in zip(*map(str.strip,open("input.txt")))];R=[*range(len(M))]
for i in R:
 while"O."in M[i]:M[i]=M[i].replace("O.",".O")
print(sum(sum(M[j][i]>'A'for j in R)*(i+1)for i in R))
