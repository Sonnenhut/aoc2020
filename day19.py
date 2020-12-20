import re


def part1():
    blocks = open("inputs/day19.txt").read().split("\n\n")
    rgx = expand(parse_rules(blocks[0]))
    return sum([re.match(rgx, t) is not None for t in blocks[1].splitlines()])


def part2():
    blocks = open("inputs/day19.txt").read().split("\n\n")
    rules = parse_rules(blocks[0])

    # 8: 42 | 42 8
    # loops 42 at least one or more times
    rules[8] = "( 42 ){1,}"

    # 11: 42 31 | 42 11 31
    # basically 42 31 loops where it can occur again: "42 (42 (..) 31) 31", but has to occur at least like "42 31"
    # not really "infinite" as per description, but matches all examples just as fine
    rules[11] = "( 42 ( 42 ( 42 ( 42 ( 42 ( 42 31 ){0,1} 31 ){0,1} 31 ){0,1} 31 ){0,1} 31 ){0,1} 31 ){1}"

    rgx = expand(rules)
    return sum([re.match(rgx, test) is not None for test in blocks[1].splitlines()])


def parse_rules(text):
    lines = sorted(text.splitlines(), key=lambda line: int(line.split(":")[0]))
    size = int(lines[-1].split(":")[0]) + 1

    rules = [""] * size
    rules[0] = lines[0].split(": ")[1]
    for line in lines[1:]:
        idx, line = line.split(": ")
        idx = int(idx)
        line = line.replace("\"", "")
        if "|" in line:
            rules[idx] = "( " + line + " )"
        else:
            rules[idx] = line
    return rules


def expand(rules):
    while any(c.isdigit() for c in rules[0].split(" ")):
        expanded = []
        for c in rules[0].split(" "):
            newc = c
            if c.isdigit():
                newc = rules[int(c)]
            expanded.append(newc)
        rules[0] = " ".join(expanded)
    return "^" + rules[0].replace(" ", "") + "$"


# 171
print(part1())
# 369
print(part2())
