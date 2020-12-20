S={int(''.join(dict(zip("FBLR","0101"))[c]for c in n.strip()),2)for n in open("input.txt")}
for n in S:
 if n+2in S and not n+1in S:print n+1
