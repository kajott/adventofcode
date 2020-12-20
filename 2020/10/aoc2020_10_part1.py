N=[0]+sorted(map(int,open("input.txt")))
D=[b-a for a,b in zip(N,N[1:])]
print(D.count(3)+1)*D.count(1)
