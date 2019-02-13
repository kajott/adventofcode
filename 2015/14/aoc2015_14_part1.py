t=2503
print max(s*(t/(f+r)*f+min(f,t%(f+r)))for s,f,r in((int(l.split()[i])for i in(3,6,13))for l in open("input.txt")))
