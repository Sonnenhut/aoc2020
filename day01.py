def parse_input(filename):
    return sorted(list(map(int, open(filename, "r").read().splitlines())))


def pt1():
    inp = parse_input("inputs/day01.txt")
    for ex1 in inp:
        for ex2 in inp:
            if ex1 + ex2 == 2020:
                return ex1 * ex2
    return -1


def pt2():
    inp = parse_input("inputs/day01.txt")
    for ex1 in inp:
        for ex2 in inp:
            for ex3 in inp:
                if ex1 + ex2 + ex3 == 2020:
                    return ex1 * ex2 * ex3
    return -1


# 1014171
print(pt1())
# 46584630
print(pt2())
