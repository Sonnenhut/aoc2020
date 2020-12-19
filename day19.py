import re


def part1():
    blocks = open("inputs/day19.txt").read().split("\n\n")
    rgx = rules_to_regex(blocks[0])
    tests = blocks[1].splitlines()
    print(rgx)
    return sum([re.match(rgx, t) is not None for t in tests])


def rules_to_regex(text):
    lines = sorted(text.splitlines(), key=lambda line: int(line.split(":")[0]))
    rules = ["(" + line.split(":")[1].replace(" ", "") + ")" for line in lines]
    rules = [rule.replace("(\"", "").replace("\")", "") for rule in rules]

    # expand substitutions
    while any(c.isdigit() for c in rules[0]):

        print("i", len(rules[0]))
        expanded = []
        for c in rules[0]:
            newc = c
            if newc.isdigit():
                newc = rules[int(c)]
            expanded += newc
        rules[0] = "".join(expanded)
    print(rules)
    return "^" + rules[0] + "$"


print(part1())
