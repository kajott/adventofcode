#!/usr/bin/env python3
"AoC 2024/21"
import functools

def generate_keymap(keys):
    return {key:(x,y) for y,row in enumerate(keys.split()) for x,key in enumerate(row)}
keymaps = [
    generate_keymap("789 456 123 x0A"),
    generate_keymap("x^A <v>")
]

@functools.cache
def search(sequence, pad_no, max_pads):
    if pad_no > max_pads:
        return len(sequence)
    keymap = keymaps[pad_no > 0]
    px, py = keymap['A']
    ix, iy = keymap['x']
    result = 0
    for key in sequence:
        tx, ty = keymap[key]
        queue = [(px, py, "")]
        paths = []
        while queue:
            cx, cy, path = queue.pop()
            if (cx, cy) == (tx, ty):
                paths.append(path + 'A')
                continue
            if (cx, cy) == (ix, iy):
                continue
            if tx < cx: queue.append((cx-1, cy, path + '<'))
            if tx > cx: queue.append((cx+1, cy, path + '>'))
            if ty < cy: queue.append((cx, cy-1, path + '^'))
            if ty > cy: queue.append((cx, cy+1, path + 'v'))
        result += min(search(path, pad_no + 1, max_pads) for path in paths)
        px, py = tx, ty
    return result

def run(max_pads, verbose=False):
    result = 0
    for line in open("input.txt"):
        sequence = line.strip()
        value = int(sequence[:-1])
        length = search(sequence, 0, max_pads)
        score = length * value
        if verbose:
            print(sequence + ":", length, "*", value, "=", score)
        result += score
    print(result)

if __name__ == "__main__":
    run(2)
    run(25)
