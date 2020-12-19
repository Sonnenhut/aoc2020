import re


def part1():
    blocks = open("inputs/day19.txt").read().split("\n\n")
    rules = parse_rules(blocks[0])
    tests = blocks[1].splitlines()
    res = 0
    for test in tests:
        matches, remainder = is_valid(test, rules, 0)
        res += matches and len(remainder) == 0
    return res
    #return sum([is_valid(test, rules, 0) for test in tests])0


def is_valid(test, rules, idx):
    possibles = [rules[idx]]
    if "|" in rules[idx]:
        possibles = rules[idx].split("|")

    one_side_matches = False
    test_remain = test
    while one_side_matches is False and len(possibles):
        test_remain = test
        possible_matches = True
        for c in possibles.pop():
            if c.isdigit():
                valid, test_remain = is_valid(test_remain, rules, int(c))
                possible_matches &= valid
                if not possible_matches:
                    break
            elif c == " ":
                continue
            elif c.isalpha():
                if len(test) == 0:
                    return False, test
                else:
                    return test[0] == c, test[min(len(test), 1):]
        one_side_matches |= possible_matches
    return one_side_matches, test_remain


def parse_rules(text):
    lines = sorted(text.splitlines(), key=lambda line: int(line.split(":")[0]))
    rules = [line.split(":")[1].replace(" ", "") for line in lines]
    return rules


print(part1())
