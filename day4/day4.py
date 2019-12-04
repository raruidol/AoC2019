def check_multi_num(num):
    multi_num_found = False
    sequence = [int(x) for x in str(num)]
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i+1]:
            multi_num_found = True

    return multi_num_found


def check_multi_num_aux(num):
    if int(num[0]) == int(num[1]):
        return True

    return False


def check_double_num(num):
    s_num = str(num)
    pair_seq = []
    res = []

    for i in range(len(s_num)-1):
        pair_seq.append(s_num[i]+s_num[i+1])

    for n in pair_seq:
        res.append(check_multi_num_aux(n))

    for t in range(len(res)-1):
        if t == 0:
            if res[t] == True and res[t+1] == False:
                return True

        if t > 0 and t != len(res)-2:
            if res[t-1] == False and res[t] == True and res[t+1] == False:
                return True

        if t == len(res)-2:
            if res[t] == False and res[t+1] == True:
                return True

            elif res[t-1] == False and res[t] == True and res[t+1] == False:
                return True

    return False

def check_no_decrease(num):
    sequence = [int(x) for x in str(num)]
    for i in range(len(sequence)-1):
        if sequence[i]>sequence[i+1]:
            return False

    return True

if __name__ == "__main__":
    f = open("../inputs/day4.txt", "r")

    rng = f.readline().split('-')
    ini = int(rng[0])
    end = int(rng[1])

    n_pwds1 = 0
    n_pwds2 = 0

    for pwd in range(ini, end+1):

        print('Checking password: ', pwd)

        # PART 1
        if check_multi_num(pwd) and check_no_decrease(pwd):
            n_pwds1 += 1

        # PART 2
        if check_double_num(pwd) and check_no_decrease(pwd):
            n_pwds2 += 1


    print('The number of possible passwords (PART 1) within that range is: ', n_pwds1)
    print('The number of possible passwords (PART 2) within that range is: ', n_pwds2)
