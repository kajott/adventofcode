print(sum(eval(p[-1].join(p[:-1]))for p in zip(*(l.split()for l in open("input.txt")))))
