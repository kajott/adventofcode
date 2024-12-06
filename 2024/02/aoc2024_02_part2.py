C=lambda r:(min(d:=[a-b for a,b in zip(r,r[1:])])*max(d)>0)*(max(map(abs,d))<4)
print(sum(any(C(r[:i]+r[i+1:])for i in range(len(r)))for r in([*map(int,l.split())]for l in open("input.txt"))))
