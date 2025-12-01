#!/usr/bin/env python3

if __name__ == "__main__":
    pos = 50
    res1 = res2 = 0
    for line in open("input.txt"):
        n = int(line[1:])
        res2 += n // 100
        n = n % 100
        newpos = pos + n * { 'L':-1, 'R':1 }[line[0]]
        res2 += (pos > 0) and ((newpos <= 0) or (newpos > 99))
        pos = newpos % 100
        res1 += not(pos)
    print(res1)
    print(res2)
