print''.join(max((c.count(x),x)for x in set(c))[1]for c in zip(*open("input.txt"))).strip()
