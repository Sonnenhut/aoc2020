import functools


def parse_input(file_name):
    return list(sorted(map(int, open(file_name, "r").read().splitlines())))


def part1():
    adapters = parse_input("inputs/day10.txt")
    adapter_combinations = zip([0] + adapters, adapters + [max(adapters) + 3])
    differences = list(map(lambda pair: pair[1] - pair[0], adapter_combinations))

    return differences.count(1) * differences.count(3)


@functools.cache
def count_chain_combinations(given_jolt, adapters):
    res = 0
    next_adapters = set(adapters) & set(range(given_jolt + 1, given_jolt + 4))
    for next_adapter in next_adapters:
        down = count_chain_combinations(next_adapter, adapters)
        res += down

    if len(next_adapters) == 0:
        # chain reached the end, increase the count!
        res += 1

    return res


def part2():
    adapters = parse_input("inputs/day10.txt")
    adapter_combinations = [0] + adapters + [max(adapters) + 3]
    return count_chain_combinations(0, frozenset(adapter_combinations))


# 1917
print(part1())
# 113387824750592
print(part2())
