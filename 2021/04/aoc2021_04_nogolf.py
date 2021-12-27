#!/usr/bin/env python3

win_sets = []
for x in range(5):
    win_sets.append({*range(x*5, x*5+5)})
    win_sets.append({*range(x, 25, 5)})

class Board:
    def __init__(self, lines):
        self.numbers = list(map(int, ' '.join(lines).split()))
        assert len(self.numbers) == 25
        self.marked = set()
        self.won = False
        self.lastmark = 0

    def mark(self, n):
        try:
            self.marked.add(self.numbers.index(n))
            self.lastmark = n
            self.won = any((self.marked >= s) for s in win_sets)
            return self.won
        except ValueError:
            return False

    @property
    def score(self):
        return sum(self.numbers[i] for i in range(25) if not(i in self.marked)) * self.lastmark


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [line.strip() for line in f.read().split('\n') if line.strip()]

    draw_order = list(map(int, lines.pop(0).split(',')))
    boards = []
    while lines:
        boards.append(Board(lines[:5]))
        del lines[:5]

    first_win = None
    last_win = None
    while not all(b.won for b in boards):
        draw = draw_order.pop(0)
        for b in boards:
            if not(b.won) and b.mark(draw):
                last_win = b
                if not first_win: first_win = b
    print(first_win.score)
    print(last_win.score)
