M=lambda a:set(range(a,99))
G={"children":{3},"cats":M(8),"samoyeds":{2},"pomeranians":{0,1,2},"akitas":{0},"vizslas":{0},"goldfish":{0,1,2,3,4},"trees":M(4),"cars":{2},"perfumes":{1}}
print max((sum(int(n)in G[x]for x,n in zip(w[2::2],w[3::2])),int(w[1]))for w in(l.translate(None,":,").split()for l in open("input.txt")))[1]
