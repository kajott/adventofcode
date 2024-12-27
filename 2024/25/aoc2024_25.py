E=enumerate
M=[{(x,y)for y,l in E(s.split('\n'))for x,c in E(l)if'.'>c}for s in open("input.txt").read().split('\n\n')]
print(sum(not(a&b)for a in M for b in M)//2)
