# Part 1 or 2 of the problem
PART = 2

def add(code, s1, s2, dest):
    sum = code[s1]+code[s2]
    code[dest] = sum
    return code

def mult(code, m1, m2, dest):
    mult = code[m1]*code[m2]
    code[dest] = mult
    return code

def run(code, n, v):
    code[1] = n
    code[2] = v

    index = 0

    while True:

        op = code[index]
        p1 = code[index + 1]
        p2 = code[index + 2]
        p3 = code[index + 3]

        if op == 1:
            code = add(code, p1, p2, p3)

        elif op == 2:
            code = mult(code, p1, p2, p3)

        elif op == 99:
            break

        index += 4
    return code[0]


if __name__ == "__main__":
    f = open("../inputs/day2/day2.txt", "r")

    l = f.readline().split(',')
    prog = [int(i) for i in l]

    # PART 1: execute the code for the input parameters noun (12) and verb (2)
    if PART == 1:
        noun = 12
        verb = 2
        code = [i for i in prog]

        res = run(code, noun, verb)

        print('The result of the code with noun: ', noun, 'and verb: ', verb, 'is: ', res)

    # PART 2: determine noun and verb to obtain output 19690720
    elif PART == 2:
        for noun in range(0,100):
            for verb in range(0,100):
                code = [i for i in prog]
                res = run(code, noun, verb)
                if res == 19690720:
                    print('Noun: ', noun,' Verb: ', verb)
                    print(100*noun+verb)
                    break


