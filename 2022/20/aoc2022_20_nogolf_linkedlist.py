#!/usr/bin/env python3

class Number:
    def __init__(self, value, prev):
        self.value = value
        self.next = None
        if prev:
            prev.next = self

def iterate_list(item):
    while item:
        yield item
        item = item.next

def mixing_round(item, data):
    while item:
        oldidx = data.index(item)
        del data[oldidx]
        newidx = (oldidx + item.value) % len(data)
        data.insert(newidx, item)
        #print(item.value, ':', oldidx, '->', newidx, '==>', [n.value for n in data])
        item = item.next

def run_part(first_item, rounds):
    data = list(iterate_list(first_item))
    for r in range(rounds):
        mixing_round(first, data)
    data = [n.value for n in data]
    zero = data.index(0)
    print(sum(data[(zero + i) % len(data)] for i in range(1000, 3001, 1000)))

if __name__ == "__main__":
    first = None
    item = None
    for n in map(int, open("input.txt")):
    #for n in [1, 2, -3, 3, -2, 0, 4]:
        item = Number(n, item)
        if not first: first = item

    run_part(first, 1)

    for item in iterate_list(first):
        item.value *= 811589153

    run_part(first, 10)
