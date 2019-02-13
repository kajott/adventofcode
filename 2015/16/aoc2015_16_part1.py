G={"children":3,"cats":7,"samoyeds":2,"pomeranians":3,"akitas":0,"vizslas":0,"goldfish":5,"trees":3,"cars":2,"perfumes":1}
print max((sum(G[x]==int(n)for x,n in zip(w[2::2],w[3::2])),int(w[1]))for w in(l.translate(None,":,").split()for l in open("input.txt")))[1]
