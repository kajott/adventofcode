import scipy.optimize as O;G=0
for L in open("input.txt"):B=[[*map(int,p[1:-1].split(','))]for p in L.split()[1:]];T=B.pop();G+=round(O.linprog([1]*len(B),A_eq=[[r in b for b in B]for r in range(len(T))],b_eq=T,integrality=1).fun)
print(G)
