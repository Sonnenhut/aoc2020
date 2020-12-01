input = sorted(list(map(int, open("inputs/day01.txt", "r").read().splitlines())))


def pt1():
    for ex1 in input:
        for ex2 in input:
            if ex1 + ex2 == 2020:
                return ex1 * ex2
    return -1


def pt2():
    for ex1 in input:
        for ex2 in input:
            for ex3 in input:
                if ex1 + ex2 + ex3 == 2020:
                    return ex1 * ex2 * ex3
    return -1


# 1014171
print(pt1())
# 46584630
print(pt2())
