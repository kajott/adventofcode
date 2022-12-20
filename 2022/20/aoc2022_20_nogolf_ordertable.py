#!/usr/bin/env python3

def solve(numbers, rounds):
    order = list(range(len(numbers)))
    for raw_index in order * rounds:
        index = order.index(raw_index)
        value = numbers[order.pop(index)]
        index = (index + value) % len(order)
        order.insert(index, raw_index)
    if 0:
        print("numbers:", numbers)
        print("order:", order)
        print("shuffled:", [numbers[i] for i in order])
    zero = order.index(numbers.index(0))
    print(sum(numbers[order[(zero + i) % len(order)]] for i in range(1000, 3001, 1000)))

if __name__ == "__main__":
    numbers = list(map(int, open("input.txt")))
    solve(numbers, 1)
    solve([n * 811589153 for n in numbers], 10)
