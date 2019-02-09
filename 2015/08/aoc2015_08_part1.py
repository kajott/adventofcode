print sum(len(l.strip())-len(eval(l))for l in open("input.txt"))
