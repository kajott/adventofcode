print max(int(''.join(dict(zip("FBLR","0101"))[c]for c in n.strip()),2)for n in open("input.txt"))
