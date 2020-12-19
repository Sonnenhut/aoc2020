import re


def part1():
    blocks = open("inputs/day19t.txt").read().split("\n\n")
    rules = parse_rules(blocks[0])
    tests = blocks[1].splitlines()
    res = 0
    for test in tests:
        res += is_valid(test, rules, 0)
    return res


def part2():
    blocks = open("inputs/day19t.txt").read().split("\n\n")
    rules = parse_rules(blocks[0])
    tests = blocks[1].splitlines()
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    res = 0
    for test in tests:
        res += is_valid(test, rules, 0)
    return res


def is_valid(test, rules, rule_idx):
    rule = rules[rule_idx]

    remainder = test
    for delegate in rule.strip().split(" "):
        found = check_recursive(remainder, rules, int(delegate))
        #print("rule {} found {}".format(delegate, found))
        if len(found):
            remainder = remainder[len(found):]
        else:
            break
    return len(remainder) == 0


def check_recursive(test, rules, rule_idx):
    rule = rules[rule_idx]
    match = []
    subrules = rule.split("|")
    while subrules:
        check = subrules.pop()
        match = []
        for c in check.strip().split(" "):
            if c.isdigit():
                match_part = check_recursive(test[len(match):], rules, int(c))
                if len(match_part):
                    match += match_part
                else:
                    match = []
                    break
            elif c.isalpha():
                if test[0] == c:
                    return test[0]
                else:
                    return ""
        if match:
            # when one subrule matches, don't even try looking at the other one...
            subrules = []
    #print("return match for rule", rule, match)
    return match


def parse_rules(text):
    lines = sorted(text.splitlines(), key=lambda line: int(line.split(":")[0]))
    res = {int(line.split(":")[0]): line.split(":")[1].replace("\"", "") for line in lines}
    return res


# 171
#print(part1())


print("part2",part2())


exec('def foo(): print("test")')
exec("foo()")
