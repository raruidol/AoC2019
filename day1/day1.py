# Part 1 or 2 of the problem
PART = 1


def get_fuel(mass):
    f = int(int(mass)/3)-2
    return f


if __name__ == "__main__":
    f = open("../inputs/day1.txt", "r")

    res = 0

    for mass in f:

        if PART == 1:
            fuel = get_fuel(mass)
            res += fuel

        else:
            while True:

                fuel = get_fuel(mass)

                if fuel == 0 or fuel < 0:
                    break

                res += fuel
                mass = fuel

    print(res)
