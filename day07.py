import re

def parse_file(name):
    lines = open(name, "r").read().splitlines()
    res = {}
    for line in lines:
        name, contained = line.split(" bags contain ")
        contained = map(lambda c: (c[:1], re.sub(" (bags|bag)[.]?", "", c[2:])), contained.split(", "))
        contained = list(filter(lambda o: "other" not in o[1], contained))
        res[name] = contained
    return res


# @functools.cache could squeeze out a bit of performance here
def flatten_bag(name, rules, override_amt=None):
    res = []
    for (amt, contained_name) in rules[name]:
        if override_amt is not None:
            amt = override_amt
        res.extend([contained_name] * int(amt))
        res.extend(flatten_bag(contained_name, rules, override_amt) * int(amt))
    return res


def part1(name):
    rules = parse_file("inputs/day07.txt")
    res = 0
    for rule in rules:
        if name in flatten_bag(rule, rules, 1):
            res += 1
    return res


def part2(name):
    rules = parse_file("inputs/day07.txt")
    return len(flatten_bag(name, rules))


# 169
print(part1("shiny gold"))
# 82372
print(part2("shiny gold"))
