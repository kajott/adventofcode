t,d=(int(''.join(l.split()[1:]))for l in open("input.txt"))
print(sum(d<h*(t-h)for h in range(t)))
