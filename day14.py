import re
import functools
import itertools


def part1():
    mem = {}
    to_0, to_1 = [], []
    for line in open("inputs/day14.txt").read().splitlines():
        if "mask" in line:
            mask = line[7:]
            to_0, to_1, _ = mask_rules(mask)
        elif "mem" in line:
            idx = int(line[line.index("[") + 1:line.index("]")])
            value = int(line[line.index(" = ") + 2:])
            value = functools.reduce(lambda a, b: clear_bit(a, b), to_0, value)
            value = functools.reduce(lambda a, b: set_bit(a, b), to_1, value)
            mem[idx] = value
    return sum(mem.values())


def part2():
    mem = {}
    to_1, floating = [], []
    for line in open("inputs/day14.txt").read().splitlines():
        if "mask" in line:
            mask = line[7:]
            _, to_1, floating = mask_rules(mask)
        elif "mem" in line:
            base_idx = int(line[line.index("[") + 1:line.index("]")])
            value = int(line[line.index(" = ") + 2:])

            base_idx = functools.reduce(lambda a, b: set_bit(a, b), to_1, base_idx)
            for idx in bitwise_combinations(floating, base_idx):
                mem[idx] = value
    return sum(mem.values())


def bitwise_combinations(floating, base):
    base_zeroed = functools.reduce(lambda acc, b: clear_bit(acc, b), floating, base)
    yield base_zeroed
    for length in range(1, len(floating) + 1):
        for comb in itertools.combinations(floating, length):
            yield functools.reduce(lambda acc, b: set_bit(acc, b), comb, base_zeroed)


def mask_rules(text):
    mask_bits = text[::-1]
    positions_to_1 = [m.start() for m in re.finditer("1", mask_bits)]
    positions_to_0 = [m.start() for m in re.finditer("0", mask_bits)]
    positions_floating = [m.start() for m in re.finditer("X", mask_bits)]
    return positions_to_0, positions_to_1, positions_floating


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


# 12135523360904
print(part1())
# 2741969047858
print(part2())
