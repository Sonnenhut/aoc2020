import re

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
required_fields = fields[:len(fields)-1]


def is_num_in_range(v, mini, maxi):
    try:
        i = int(v)
        return mini <= i <= maxi
    except ValueError:
        return 0

def byr(v):
    return is_num_in_range(v, 1920, 2002)


def iyr(v):
    return is_num_in_range(v, 2010, 2020)


def eyr(v):
    return is_num_in_range(v, 2020, 2030)


def hgt(v: str):
    if v.endswith("cm"):
        return is_num_in_range(v.removesuffix("cm"), 150, 193)
    elif v.endswith("in"):
        return is_num_in_range(v.removesuffix("in"), 59, 76)
    else:
        return 0


def hcl(v: str):
    return int(re.match("^#[0-9a-f]{6}$", v) is not None)


def ecl(v: str):
    return int(re.match("^amb|blu|brn|gry|grn|hzl|oth$", v) is not None)


def pid(v: str):
    return int(re.match("^[0-9]{9}$", v) is not None)


def cid(v):
    return 1


def parse_file(name):
    with open(name, "r") as f:
        input_blocks = f.read().removesuffix("\n").split("\n\n")
        inp = list(map(lambda block: re.split("[\n ]", block), input_blocks))
    return inp, input_blocks


def part1():
    _, input_blocks = parse_file("inputs/day04.txt")

    res = 0
    for input_block in input_blocks:
        contained = 1
        for wanted_field in required_fields:
            contained &= wanted_field in input_block
        res += contained
    return res


def part2():
    inp, _ = parse_file("inputs/day04.txt")

    res = 0
    for block in inp:
        block_valid = 1
        remain_fields = fields.copy()
        for single in block:
            fieldname, val = single.split(":")
            remain_fields.remove(fieldname)
            block_valid &= globals()[fieldname](val)
        block_valid &= remain_fields == ["cid"] or remain_fields == []
        res += block_valid
    return res


# 182
print(part1())
# 109
print(part2())
