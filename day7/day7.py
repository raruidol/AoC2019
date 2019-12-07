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


def run(code, inp, phase):

    ent = phase
    index = 0

    while True:

        op, rules = process(code[index])

        if op == 99:
            return v

        p1 = code[index + 1]
        p2 = code[index + 2]
        p3 = code[index + 3]

        if op == 1:
            code = add(code, p1, p2, p3, rules)
            index += 4

        elif op == 2:
            code = mult(code, p1, p2, p3, rules)
            index += 4

        elif op == 3:
            code = store(code, p1, ent)
            ent = inp
            index += 2

        elif op == 4:
            v = retrieve(code, p1, rules)
            #print(v)
            index += 2

        elif op == 5:
            index = jump_if_true(code, p1, p2, rules, index)

        elif op == 6:
            index = jump_if_false(code, p1, p2, rules, index)

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
    for comb in itertools.permutations(range(0,5), 5):
        inp = 0
        a1 = run(prog, inp, comb[0])
        a2 = run(prog, a1, comb[1])
        a3 = run(prog, a2, comb[2])
        a4 = run(prog, a3, comb[3])
        a5 = run(prog, a4, comb[4])
        inp = a5

        if a5 > max_signal:
            max_signal = a5


        print('The highest signal that can be sent to the thrusters ', comb, 'is: ', a5)

    print('The highest signal that can be sent to the thrusters is: ', max_signal)
