print(sum(max(int(a+b)for i,a in enumerate(n,1)for b in n[i:])for n in open("input.txt")))
