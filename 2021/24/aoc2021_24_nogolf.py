#!/usr/bin/env python3
import random

def div(a, b):
    r = abs(a) // abs(b)
    return r if ((a >= 0) and (b > 0)) else -r

def monad_unopt(input):
    x = y = z = w = 0
    w = input[0]         # [001] inp w
    x = 0                # [002] mul x 0
    x += z               # [003] add x z
    x = x % 26           # [004] mod x 26
    z = div(z, 1)        # [005] div z 1
    x += 12              # [006] add x 12
    x = (x == w)         # [007] eql x w
    x = not(x)           # [008] eql x 0
    y = 0                # [009] mul y 0
    y += 25              # [010] add y 25
    y *= x               # [011] mul y x
    y += 1               # [012] add y 1
    z *= y               # [013] mul z y
    y = 0                # [014] mul y 0
    y += w               # [015] add y w
    y += 9               # [016] add y 9
    y *= x               # [017] mul y x
    z += y               # [018] add z y
    w = input[1]         # [019] inp w
    x = 0                # [020] mul x 0
    x += z               # [021] add x z
    x = x % 26           # [022] mod x 26
    z = div(z, 1)        # [023] div z 1
    x += 12              # [024] add x 12
    x = (x == w)         # [025] eql x w
    x = not(x)           # [026] eql x 0
    y = 0                # [027] mul y 0
    y += 25              # [028] add y 25
    y *= x               # [029] mul y x
    y += 1               # [030] add y 1
    z *= y               # [031] mul z y
    y = 0                # [032] mul y 0
    y += w               # [033] add y w
    y += 4               # [034] add y 4
    y *= x               # [035] mul y x
    z += y               # [036] add z y
    w = input[2]         # [037] inp w
    x = 0                # [038] mul x 0
    x += z               # [039] add x z
    x = x % 26           # [040] mod x 26
    z = div(z, 1)        # [041] div z 1
    x += 12              # [042] add x 12
    x = (x == w)         # [043] eql x w
    x = not(x)           # [044] eql x 0
    y = 0                # [045] mul y 0
    y += 25              # [046] add y 25
    y *= x               # [047] mul y x
    y += 1               # [048] add y 1
    z *= y               # [049] mul z y
    y = 0                # [050] mul y 0
    y += w               # [051] add y w
    y += 2               # [052] add y 2
    y *= x               # [053] mul y x
    z += y               # [054] add z y
    w = input[3]         # [055] inp w
    x = 0                # [056] mul x 0
    x += z               # [057] add x z
    x = x % 26           # [058] mod x 26
    z = div(z, 26)       # [059] div z 26
    x -= 9               # [060] add x -9
    x = (x == w)         # [061] eql x w
    x = not(x)           # [062] eql x 0
    y = 0                # [063] mul y 0
    y += 25              # [064] add y 25
    y *= x               # [065] mul y x
    y += 1               # [066] add y 1
    z *= y               # [067] mul z y
    y = 0                # [068] mul y 0
    y += w               # [069] add y w
    y += 5               # [070] add y 5
    y *= x               # [071] mul y x
    z += y               # [072] add z y
    w = input[4]         # [073] inp w
    x = 0                # [074] mul x 0
    x += z               # [075] add x z
    x = x % 26           # [076] mod x 26
    z = div(z, 26)       # [077] div z 26
    x -= 9               # [078] add x -9
    x = (x == w)         # [079] eql x w
    x = not(x)           # [080] eql x 0
    y = 0                # [081] mul y 0
    y += 25              # [082] add y 25
    y *= x               # [083] mul y x
    y += 1               # [084] add y 1
    z *= y               # [085] mul z y
    y = 0                # [086] mul y 0
    y += w               # [087] add y w
    y += 1               # [088] add y 1
    y *= x               # [089] mul y x
    z += y               # [090] add z y
    w = input[5]         # [091] inp w
    x = 0                # [092] mul x 0
    x += z               # [093] add x z
    x = x % 26           # [094] mod x 26
    z = div(z, 1)        # [095] div z 1
    x += 14              # [096] add x 14
    x = (x == w)         # [097] eql x w
    x = not(x)           # [098] eql x 0
    y = 0                # [099] mul y 0
    y += 25              # [100] add y 25
    y *= x               # [101] mul y x
    y += 1               # [102] add y 1
    z *= y               # [103] mul z y
    y = 0                # [104] mul y 0
    y += w               # [105] add y w
    y += 6               # [106] add y 6
    y *= x               # [107] mul y x
    z += y               # [108] add z y
    w = input[6]         # [109] inp w
    x = 0                # [110] mul x 0
    x += z               # [111] add x z
    x = x % 26           # [112] mod x 26
    z = div(z, 1)        # [113] div z 1
    x += 14              # [114] add x 14
    x = (x == w)         # [115] eql x w
    x = not(x)           # [116] eql x 0
    y = 0                # [117] mul y 0
    y += 25              # [118] add y 25
    y *= x               # [119] mul y x
    y += 1               # [120] add y 1
    z *= y               # [121] mul z y
    y = 0                # [122] mul y 0
    y += w               # [123] add y w
    y += 11              # [124] add y 11
    y *= x               # [125] mul y x
    z += y               # [126] add z y
    w = input[7]         # [127] inp w
    x = 0                # [128] mul x 0
    x += z               # [129] add x z
    x = x % 26           # [130] mod x 26
    z = div(z, 26)       # [131] div z 26
    x -= 10              # [132] add x -10
    x = (x == w)         # [133] eql x w
    x = not(x)           # [134] eql x 0
    y = 0                # [135] mul y 0
    y += 25              # [136] add y 25
    y *= x               # [137] mul y x
    y += 1               # [138] add y 1
    z *= y               # [139] mul z y
    y = 0                # [140] mul y 0
    y += w               # [141] add y w
    y += 15              # [142] add y 15
    y *= x               # [143] mul y x
    z += y               # [144] add z y
    w = input[8]         # [145] inp w
    x = 0                # [146] mul x 0
    x += z               # [147] add x z
    x = x % 26           # [148] mod x 26
    z = div(z, 1)        # [149] div z 1
    x += 15              # [150] add x 15
    x = (x == w)         # [151] eql x w
    x = not(x)           # [152] eql x 0
    y = 0                # [153] mul y 0
    y += 25              # [154] add y 25
    y *= x               # [155] mul y x
    y += 1               # [156] add y 1
    z *= y               # [157] mul z y
    y = 0                # [158] mul y 0
    y += w               # [159] add y w
    y += 7               # [160] add y 7
    y *= x               # [161] mul y x
    z += y               # [162] add z y
    w = input[9]         # [163] inp w
    x = 0                # [164] mul x 0
    x += z               # [165] add x z
    x = x % 26           # [166] mod x 26
    z = div(z, 26)       # [167] div z 26
    x -= 2               # [168] add x -2
    x = (x == w)         # [169] eql x w
    x = not(x)           # [170] eql x 0
    y = 0                # [171] mul y 0
    y += 25              # [172] add y 25
    y *= x               # [173] mul y x
    y += 1               # [174] add y 1
    z *= y               # [175] mul z y
    y = 0                # [176] mul y 0
    y += w               # [177] add y w
    y += 12              # [178] add y 12
    y *= x               # [179] mul y x
    z += y               # [180] add z y
    w = input[10]        # [181] inp w
    x = 0                # [182] mul x 0
    x += z               # [183] add x z
    x = x % 26           # [184] mod x 26
    z = div(z, 1)        # [185] div z 1
    x += 11              # [186] add x 11
    x = (x == w)         # [187] eql x w
    x = not(x)           # [188] eql x 0
    y = 0                # [189] mul y 0
    y += 25              # [190] add y 25
    y *= x               # [191] mul y x
    y += 1               # [192] add y 1
    z *= y               # [193] mul z y
    y = 0                # [194] mul y 0
    y += w               # [195] add y w
    y += 15              # [196] add y 15
    y *= x               # [197] mul y x
    z += y               # [198] add z y
    w = input[11]        # [199] inp w
    x = 0                # [200] mul x 0
    x += z               # [201] add x z
    x = x % 26           # [202] mod x 26
    z = div(z, 26)       # [203] div z 26
    x -= 15              # [204] add x -15
    x = (x == w)         # [205] eql x w
    x = not(x)           # [206] eql x 0
    y = 0                # [207] mul y 0
    y += 25              # [208] add y 25
    y *= x               # [209] mul y x
    y += 1               # [210] add y 1
    z *= y               # [211] mul z y
    y = 0                # [212] mul y 0
    y += w               # [213] add y w
    y += 9               # [214] add y 9
    y *= x               # [215] mul y x
    z += y               # [216] add z y
    w = input[12]        # [217] inp w
    x = 0                # [218] mul x 0
    x += z               # [219] add x z
    x = x % 26           # [220] mod x 26
    z = div(z, 26)       # [221] div z 26
    x -= 9               # [222] add x -9
    x = (x == w)         # [223] eql x w
    x = not(x)           # [224] eql x 0
    y = 0                # [225] mul y 0
    y += 25              # [226] add y 25
    y *= x               # [227] mul y x
    y += 1               # [228] add y 1
    z *= y               # [229] mul z y
    y = 0                # [230] mul y 0
    y += w               # [231] add y w
    y += 12              # [232] add y 12
    y *= x               # [233] mul y x
    z += y               # [234] add z y
    w = input[13]        # [235] inp w
    x = 0                # [236] mul x 0
    x += z               # [237] add x z
    x = x % 26           # [238] mod x 26
    z = div(z, 26)       # [239] div z 26
    x -= 3               # [240] add x -3
    x = (x == w)         # [241] eql x w
    x = not(x)           # [242] eql x 0
    y = 0                # [243] mul y 0
    y += 25              # [244] add y 25
    y *= x               # [245] mul y x
    y += 1               # [246] add y 1
    z *= y               # [247] mul z y
    y = 0                # [248] mul y 0
    y += w               # [249] add y w
    y += 12              # [250] add y 12
    y *= x               # [251] mul y x
    z += y               # [252] add z y
    return z

cD = [1, 1, 1, 26, 26, 1, 1, 26, 1, 26, 1, 26, 26, 26]; assert len(cD) == 14
cM = [12, 12, 12, -9, -9, 14, 14, -10, 15, -2, 11, -15, -9, -3];  assert len(cM) == 14
cA = [9, 4, 2, 5, 1, 6, 11, 15, 7, 12, 15, 9, 12, 12];  assert len(cA) == 14

def monad_opt(input, use_opt=False):
    x = z = 0
    opt = input[:]
    for r in range(14):
        w = input[r]
        checkval = z % 26 + cM[r]
        z //= cD[r]
        if opt:
            if 1 <= checkval <= 9:
                opt[r] = checkval
                if use_opt: w = checkval
            elif cD[r] > 1:
                opt = None
        if checkval != w:
            z = z * 26 + w + cA[r]
    return z, opt

if __name__ == "__main__":
    i = 0
    vmin = [10]
    vmax = [0]
    while True:
        j = i
        seq = [0] * 14
        for r in range(14):
            if cD[r] < 26:
                seq[r] = 1 + (j % 9)
                j //= 9
        if j: break
        z, opt = monad_opt(seq, True)
        if not z:
            if (opt > vmax) or (opt < vmin): print(opt)
            if opt > vmax: vmax = opt
            if opt < vmin: vmin = opt
        i += 1
    print(''.join(map(str, vmax)))
    print(''.join(map(str, vmin)))

if __name__ == "verify_minified_code":
    random.seed(0x13375EED)
    opt = None
    while True:
        if opt:
            seq = opt
            print("opt:", seq)
        else:
            seq = [random.randrange(1,2) for n in range(14)]
            print("new:", seq)
        ref = monad_unopt(seq)
        dut, opt = monad_opt(seq)
        if ref != dut:
            print(f"DEVIATION FOUND! {ref=} {dut=}")
        if not(ref) or not(dut):
            print("VALID CODE:", ''.join(map(str, seq)))
        if opt and (opt == seq):
            opt = None
