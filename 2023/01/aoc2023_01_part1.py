print(sum(int(n[0]+n[-1])for n in([*filter(str.isdigit,l)]for l in open("input.txt"))))
