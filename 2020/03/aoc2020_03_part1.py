print sum(r[(3*y)%len(r)]for y,r in enumerate([c<'.'for c in l.strip()]for l in open("input.txt")))
