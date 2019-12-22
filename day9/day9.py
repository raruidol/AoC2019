def add(code, s1, s2, dest, r, base):
    x1 = None
    x2 = None
    if r[0] == 0:
        x1 = code[s1]
    elif r[0] == 1:
        x1 = s1
    elif r[0] == 2:
        x1 = code[code[s1]+base]

    if r[1] == 0:
        x2 = code[s2]
    elif r[1] == 1:
        x2 = s2
    elif r[1] == 2:
        x2 = code[code[s2]+base]

    if r[2] == 0:
        code[dest] = x1 + x2
    elif r[2] == 2:
        code[code[dest]+base] = x1 + x2

    return code


def mult(code, m1, m2, dest, r, base):
    x1 = None
    x2 = None
    if r[0] == 0:
        x1 = code[m1]
    elif r[0] == 1:
        x1 = m1
    elif r[0] == 2:
        x1 = code[code[m1]+base]

    if r[1] == 0:
        x2 = code[m2]
    elif r[1] == 1:
        x2 = m2
    elif r[1] == 2:
        x2 = code[code[m2]+base]

    if r[2] == 0:
        code[dest] = x1 * x2
    elif r[2] == 2:
        code[code[dest]+base] = x1 * x2

    return code


def store(code, dir, val, r, base):
    if r[0] == 0:
        code[dir] = val
    elif r[0] == 2:
        code[code[dir]+base] = val

    return code


def retrieve(code, dir, r, base):
    x1 = None
    if r[0] == 0:
        x1 = code[dir]
    elif r[0] == 1:
        x1 = dir
    elif r[0] == 2:
        x1 = code[code[dir]+base]

    return x1


def jump_if_true(code, p1, p2, r, index, base):
    i = index+3
    x1 = None

    if r[0] == 0:
        x1 = code[p1]
    elif r[0] == 1:
        x1 = p1
    elif r[0] == 2:
        x1 = code[code[p1]+base]

    if x1 != 0:
        if r[1] == 0:
            i = code[p2]
        elif r[1] == 1:
            i = p2
        elif r[1] == 2:
            i = code[code[p2]+base]

    return i


def jump_if_false(code, p1, p2, r, index, base):
    i = index+3
    x1 = None

    if r[0] == 0:
        x1 = code[p1]
    elif r[0] == 1:
        x1 = p1
    elif r[0] == 2:
        x1 = code[code[p1]+base]

    if x1 == 0:
        if r[1] == 0:
            i = code[p2]
        elif r[1] == 1:
            i = p2
        elif r[1] == 2:
            i = code[code[p2]+base]

    return i


def less_than(code, v1, v2, dest, r, base):
    x1 = None
    x2 = None
    if r[0] == 0:
        x1 = code[v1]
    elif r[0] == 1:
        x1 = v1
    elif r[0] == 2:
        x1 = code[code[v1]+base]

    if r[1] == 0:
        x2 = code[v2]
    elif r[1] == 1:
        x2 = v2
    elif r[1] == 2:
        x2 = code[code[v2]+base]

    if x1 < x2:
        if r[2] == 0:
            code[dest] = 1
        elif r[2] == 2:
            code[code[dest] + base] = 1


    else:
        if r[2] == 0:
            code[dest] = 0
        elif r[2] == 2:
            code[code[dest] + base] = 0

    return code


def equals(code, v1, v2, dest, r, base):
    x1 = None
    x2 = None
    if r[0] == 0:
        x1 = code[v1]
    elif r[0] == 1:
        x1 = v1
    elif r[0] == 2:
        x1 = code[code[v1]+base]

    if r[1] == 0:
        x2 = code[v2]
    elif r[1] == 1:
        x2 = v2
    elif r[1] == 2:
        x2 = code[code[v2]+base]

    if x1 == x2:
        if r[2] == 0:
            code[dest] = 1
        elif r[2] == 2:
            code[base + code[dest]] = 1

    else:
        if r[2] == 0:
            code[dest] = 0
        elif r[2] == 2:
            code[base + code[dest]] = 0

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


def adjust_base(code, base, p1, r):
    if r[0] == 0:
        base += code[p1]
    elif r[0] == 1:
        base += p1
    elif r[0] == 2:
        base += code[code[p1]+base]

    return base


def run(code, inp):

    index = 0
    base = 0
    v = None

    while True:

        op, rules = process(code[index])
        #print(index, base)
        #print(op, rules)

        if op == 99:
            return v

        p1 = code[index + 1]

        if op == 3:
            code = store(code, p1, inp, rules, base)
            index += 2

        elif op == 4:
            v = retrieve(code, p1, rules, base)
            print('>>',v)
            index += 2

        elif op == 9:
            base = adjust_base(code, base, p1, rules)
            index += 2

        p2 = code[index + 2]

        if op == 5:
            index = jump_if_true(code, p1, p2, rules, index, base)

        elif op == 6:
            index = jump_if_false(code, p1, p2, rules, index, base)

        p3 = code[index + 3]

        #print(p1, p2, p3)
        #print('-----')

        if op == 1:
            code = add(code, p1, p2, p3, rules, base)
            index += 4

        elif op == 2:
            code = mult(code, p1, p2, p3, rules, base)
            index += 4

        elif op == 7:
            code = less_than(code, p1, p2, p3, rules, base)
            index += 4

        elif op == 8:
            code = equals(code, p1, p2, p3, rules, base)
            index += 4


if __name__ == "__main__":
    f = open("../inputs/day9.txt", "r")

    inp = 1

    l = f.readline().split(',')
    prog = [int(i) for i in l]
    for i in range(10000):
        prog.append(0)

    res = run(prog, inp)

    print('The result of the code with input: ', inp, 'is: ', res)
