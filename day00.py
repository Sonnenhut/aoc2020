# 2019 day 1
inp = list(map(int, open("inputs/day00.txt", "r").read().splitlines()))


def fuel(mass): return mass // 3 - 2


def recursive_fuel(mass):
    res = fuel(mass)
    if res > 0:
        res += recursive_fuel(res)
    return max(0, res)


def pt1():
    total = 0
    for m in inp:
        total += fuel(m)
    return total


def pt2():
    total = 0
    for m in inp:
        total += recursive_fuel(m)
    return total


print(pt1())
print(pt2())
