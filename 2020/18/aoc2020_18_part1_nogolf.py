#!/usr/bin/env python3
import re

V = 0


def my_eval(expr):
    tokens = re.findall(r'\d+|[+*()]', expr)
    if V >= 2:
        print(expr)
        print(tokens)
    stack = [[0, "+"]]
    for token in tokens:
        if V >= 2:
            print(stack, token)
        if token == ")":
            assert len(stack[-1]) == 1
            token = str(stack.pop().pop())
        if token == "(":
            stack.append([0, "+"])
        elif token in "+*":
            assert len(stack[-1]) == 1
            stack[-1].append(token)
        else:
            token = int(token)
            assert len(stack[-1]) == 2
            if stack[-1][1] == '+':
                stack[-1][0] += token
            elif stack[-1][1] == '*':
                stack[-1][0] *= token
            else:
                assert 0
            del stack[-1][1]
    assert len(stack) == 1
    assert len(stack[-1]) == 1
    res = stack.pop().pop()
    if V >= 2:
        print()
    elif V >= 1:
        print(expr.strip(), "=", res)
    return res


if __name__ == "__main__":
    assert my_eval("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert my_eval("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert my_eval("2 * 3 + (4 * 5)") == 26
    assert my_eval("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert my_eval("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert my_eval("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

    s = 0
    for line in open("input.txt"):
        s += my_eval(line)
    print(s)
