import functools


def parse_file(name) -> []:
    with open(name, "r") as f:
        inp = f.read().removesuffix("\n").split("\n\n")
    return inp


def part1():
    res = parse_file("inputs/day06.txt")
    res = map(lambda grp: len(dict.fromkeys(grp.replace("\n", ""))), res)
    return sum(res)


def part2():
    grps = parse_file("inputs/day06.txt")
    res = 0
    for grp in grps:
        res += len(functools.reduce(lambda a, b: a.intersection(b), map(set, grp.split("\n"))))
    return res


# 6551
print(part1())
# 3358
print(part2())
