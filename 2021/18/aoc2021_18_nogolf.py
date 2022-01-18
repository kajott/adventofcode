#!/usr/bin/env python3

def import_snail(s):
    if isinstance(s, list): return s
    return [{'[':-1,']':-2}.get(x) or int(x) for x in s.strip().replace(',', '')]

def _export_snail_iter(s):
    stack = []
    for x in s:
        if (x > -2) and stack:
            if stack[-1]: yield ','
            stack[-1] += 1
        if x==-1:
            yield '['
            stack.append(0)
        elif x==-2:
            yield ']'
            stack.pop()
        else:
            yield str(x)
def export_snail(s):
    if isinstance(s, str): return s
    return ''.join(_export_snail_iter(s))


def reduce_snail(s):
    while True:
        #print("REDUCING:", export_snail(s))
        first_gt9_idx = -1
        first_l5_idx = -1
        last_pre_l5_number_idx = -1
        first_post_l5_number_idx = -1

        level = 0
        for idx, x in enumerate(s):
            if x == -1:
                level += 1
                if (level > 4) and (first_l5_idx < 0):
                    first_l5_idx = idx
            if x == -2:
                level -= 1
            if (x > 9) and (first_gt9_idx < 0):
                first_gt9_idx = idx
            if x >= 0:
                if first_l5_idx < 0:
                    last_pre_l5_number_idx = idx
                if (first_l5_idx >= 0) and (idx > (first_l5_idx + 2)):
                    first_post_l5_number_idx = idx
                    break
        #print(f"L5@{first_l5_idx} pre@{last_pre_l5_number_idx} post@{first_post_l5_number_idx} gt9@{first_gt9_idx}")

        if first_l5_idx >= 0:
            assert s[first_l5_idx+1] >= 0
            assert s[first_l5_idx+2] >= 0
            assert s[first_l5_idx+3] == -2
            if last_pre_l5_number_idx >= 0:
                s[last_pre_l5_number_idx] += s[first_l5_idx+1]
            if first_post_l5_number_idx >= 0:
                s[first_post_l5_number_idx] += s[first_l5_idx+2]
            s[first_l5_idx : first_l5_idx+4] = [0]
        elif first_gt9_idx >= 0:
            x = s[first_gt9_idx]
            s[first_gt9_idx : first_gt9_idx+1] = [-1, x//2, x-x//2, -2]
        else:
            break
    #print("RESULT:", export_snail(s))
    return s

def add(a, b):
    if not(a) or not(b): return a or b
    s = [-1] + import_snail(a) + import_snail(b) + [-2]
    return reduce_snail(s)

def add_list(lines):
    s = None
    for line in map(str.strip, lines.strip().split('\n')):
        s = add(s, line)
    return s

def test_add_list(expected, lines):
    computed = export_snail(add_list(lines))
    print("EXPECTED:", expected)
    print("COMPUTED:", computed)
    print("MAGNITUDE", magnitude(computed))
    assert expected == computed
    print()


def magnitude(s):
    s = import_snail(s)[:]
    while len(s) > 1:
        idx = 3
        while idx < len(s):
            if (s[idx-3] == -1) and (s[idx-2] >= 0) and (s[idx-1] >= 0) and (s[idx] == -2):
                s[idx-3 : idx+1] = [3*s[idx-2] + 2*s[idx-1]]
            idx += 1
    return s.pop()


if __name__ == "__main__":
    test_add_list("[[[[1,1],[2,2]],[3,3]],[4,4]]", """
        [1,1]
        [2,2]
        [3,3]
        [4,4]
    """)
    test_add_list("[[[[3,0],[5,3]],[4,4]],[5,5]]", """
        [1,1]
        [2,2]
        [3,3]
        [4,4]
        [5,5]
    """)
    test_add_list("[[[[5,0],[7,4]],[5,5]],[6,6]]", """
        [1,1]
        [2,2]
        [3,3]
        [4,4]
        [5,5]
        [6,6]
    """)
    test_add_list("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", """
        [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
        [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
        [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
        [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
        [7,[5,[[3,8],[1,4]]]]
        [[2,[2,2]],[8,[8,1]]]
        [2,9]
        [1,[[[9,3],9],[[9,0],[0,7]]]]
        [[[5,[7,4]],7],1]
        [[[[4,2],2],6],[8,7]]
    """)

    exam = test_add_list("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", """
        [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
        [[[5,[2,8]],4],[5,[[9,9],0]]]
        [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
        [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
        [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
        [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
        [[[[5,4],[7,7]],8],[[8,3],8]]
        [[9,3],[[9,9],[6,[4,9]]]]
        [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
        [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
    """)

    print(magnitude(add_list(open("input.txt").read())))

    nums = list(open("input.txt"))
    n = len(nums)
    print(max(magnitude(add(nums[a], nums[b])) for a in range(n) for b in range(n) if a != b))
