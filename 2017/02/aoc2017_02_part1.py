print sum(max(r)-min(r)for r in(map(int,r.strip().split())for r in open("input.txt")))
