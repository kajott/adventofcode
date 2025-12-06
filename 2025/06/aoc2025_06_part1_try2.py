P=lambda z:z and z[0]*P(z[1:])or 1
print(sum((P if'+'>p[-1]else sum)(list(map(int,p[:-1])))for p in zip(*(l.split()for l in open("input.txt")))))
