inp = open("inputs/day03.txt", "r").read().splitlines()


def part1(right_step, down_step):
    res = 0
    max_right = len(inp[0])
    right = right_step
    down = down_step

    while down < len(inp):
        if inp[down][right] == '#':
            res += 1
        down += down_step
        right = (right + right_step) % max_right
    return res


def part2():
    return part1(1, 1) * part1(3, 1) * part1(5, 1) * part1(7, 1) * part1(1, 2)


# 148
print(part1(3, 1))
# 727923200
print(part2())
