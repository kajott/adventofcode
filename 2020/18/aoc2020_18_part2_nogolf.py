#!/usr/bin/env python3
import re

V = 0


def my_eval(expr):
    tokens = re.findall(r'\d+|[+*()]', expr)
    if V >= 2:
        print("expr:", repr(expr))
        print("tokens:", ' '.join(tokens))

    # phase 1: use Shunting Yard Algorithm to convert infix into RPN
    ops = []
    rpn = []
    for token in tokens:
        if V >= 2:
            print(rpn, ops, token)
        if token == "(":
            ops.append(token)
        elif token == ")":
            while ops[-1] != "(":
                rpn.append(ops.pop())
            if ops[-1] == "(":
                ops.pop()
        elif token in "+*":
            while ops and (ops[-1] != "(") and ((ops[-1] == "+") and (token == "*")):
                rpn.append(ops.pop())
            ops.append(token)
        else:
            rpn.append(int(token))
    if V >= 2:
        print(rpn, ops, "END")
    while ops:
        rpn.append(ops.pop())
    if V >= 2:
        print("final RPN:", rpn)

    # phase 2: evaluate RPN
    stack = []
    for token in rpn:
        if V >= 2:
            print(stack, token)
        if token == '+':
            n = stack.pop()
            stack[-1] += n
        elif token == '*':
            n = stack.pop()
            stack[-1] *= n
        else:
            stack.append(token)
    if V >= 2:
        print(stack, "END")

    assert len(stack) == 1
    if V >= 2:
        print()
    elif V >= 1:
        print(expr.strip(), "=", stack[-1])
    return stack.pop()


if __name__ == "__main__":
    assert my_eval("1 + 2 * 3 + 4 * 5 + 6") == 231
    assert my_eval("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert my_eval("2 * 3 + (4 * 5)") == 46
    assert my_eval("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert my_eval("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert my_eval("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340

    s = 0
    for line in open("input.txt"):
        s += my_eval(line)
    print(s)
