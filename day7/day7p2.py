import itertools


def add(code, s1, s2, dest, r):
    x1 = None
    x2 = None
    if r[0] == 0:
        x1 = code[s1]
    elif r[0] == 1:
        x1 = s1

    if r[1] == 0:
        x2 = code[s2]
    elif r[1] == 1:
        x2 = s2

    sum = x1 + x2

    if r[2] == 0:
        code[dest] = sum
    elif r[2] == 1:
        code[dest] = sum

    return code


def mult(code, m1, m2, dest, r):
    x1 = None
    x2 = None
    if r[0] == 0:
        x1 = code[m1]
    elif r[0] == 1:
        x1 = m1

    if r[1] == 0:
        x2 = code[m2]
    elif r[1] == 1:
        x2 = m2

    mult = x1 * x2
    if r[2] == 0:
        code[dest] = mult
    elif r[2] == 1:
        code[dest] = mult

    return code


def store(code, dir, val):
    code[dir] = val
    return code


def retrieve(code, dir, r):
    x1 = None
    if r[0] == 0:
        x1 = code[dir]
    elif r[0] == 1:
        x1 = dir

    return x1


def jump_if_true(code, p1, p2, r, index):
    i = index+3
    x1 = None

    if r[0] == 0:
        x1 = code[p1]
    elif r[0] == 1:
        x1 = p1

    if x1 != 0:
        if r[1] == 0:
            i = code[p2]
        elif r[1] == 1:
            i = p2

    return i


def jump_if_false(code, p1, p2, r, index):
    i = index+3
    x1 = None

    if r[0] == 0:
        x1 = code[p1]
    elif r[0] == 1:
        x1 = p1

    if x1 == 0:
        if r[1] == 0:
            i = code[p2]
        elif r[1] == 1:
            i = p2

    return i


def less_than(code, v1, v2, dest, r):
    x1 = None
    x2 = None
    if r[0] == 0:
        x1 = code[v1]
    elif r[0] == 1:
        x1 = v1

    if r[1] == 0:
        x2 = code[v2]
    elif r[1] == 1:
        x2 = v2

    if x1 < x2:
        code[dest] = 1
    else:
        code[dest] = 0

    return code


def equals(code, v1, v2, dest, r):
    x1 = None
    x2 = None
    if r[0] == 0:
        x1 = code[v1]
    elif r[0] == 1:
        x1 = v1

    if r[1] == 0:
        x2 = code[v2]
    elif r[1] == 1:
        x2 = v2

    if x1 == x2:
        code[dest] = 1
    else:
        code[dest] = 0

    return code


def process(num):

    if len(str(num))>1:
        l = [i for i in str(num)]
        o1 = l.pop(-1)
        o2 = l.pop(-1)
        op = int(o2+o1)
        C = 0
        B = 0
        A = 0
        j=0
        while len(l)>0:
            if j == 0:
                C = int(l.pop(-1))
                j += 1
            elif j == 1:
                B = int(l.pop(-1))
            elif j == 2:
                A = int(l.pop(-1))

        return op, [C,B,A]
    else:
        return num, [0,0,0]


def run(code, inp, phase, ind, flag):

    if not flag:
        ent = phase
    else:
        ent = inp

    index = ind

    while True:

        op, rules = process(code[index])

        #print(op)

        if op == 99:
            end = True
            return 0, code, index, end

        #print(index)
        p1 = code[index + 1]

        if op == 3:
            code = store(code, p1, ent)
            ent = inp
            index += 2

        elif op == 4:
            v = retrieve(code, p1, rules)
            print('>>', v)
            index += 2
            end = False
            return v, code, index, end

        p2 = code[index + 2]

        if op == 5:
            index = jump_if_true(code, p1, p2, rules, index)

        elif op == 6:
            index = jump_if_false(code, p1, p2, rules, index)

        p3 = code[index + 3]

        if op == 1:
            code = add(code, p1, p2, p3, rules)
            index += 4

        elif op == 2:
            code = mult(code, p1, p2, p3, rules)
            index += 4

        elif op == 7:
            code = less_than(code, p1, p2, p3, rules)
            index += 4

        elif op == 8:
            code = equals(code, p1, p2, p3, rules)
            index += 4


if __name__ == "__main__":
    f = open("../inputs/day7.txt", "r")

    l = f.readline().split(',')
    prog = [int(i) for i in l]

    max_signal = 0

    # Try all possible phase combinations for each amplifier
    for comb in itertools.permutations(range(5,10), 5):
        c1 = prog.copy()
        c2 = prog.copy()
        c3 = prog.copy()
        c4 = prog.copy()
        c5 = prog.copy()
        i1 = i2 = i3 = i4 = i5 = 0
        f = False
        end = False
        a5 = 0
        while not end:

            a1, c1, i1, e1 = run(c1, a5, comb[0], i1, f)
            a2, c2, i2, e2 = run(c2, a1, comb[1], i2, f)
            a3, c3, i3, e3 = run(c3, a2, comb[2], i3, f)
            a4, c4, i4, e4 = run(c4, a3, comb[3], i4, f)
            a5, c5, i5, e = run(c5, a4, comb[4], i5, f)
            end = e
            inp = a5

            if a5 > max_signal:
                max_signal = a5

            f = True

    print('The highest signal that can be sent to the thrusters is: ', max_signal)
