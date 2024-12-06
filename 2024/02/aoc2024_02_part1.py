print(sum((min(d:=[a-b for a,b in zip(r,r[1:])])*max(d)>0)*(max(map(abs,d))<4)for r in([*map(int,l.split())]for l in open("input.txt"))))
