inp = open("inputs/day05.txt", "r").read().splitlines()

def binary_space_num(desc, base):
    minv = 1
    maxv = base
    for char in desc:
        space = maxv - minv + 1
        if char == 'F' or char == 'L':
            maxv = maxv - (space / 2)
        elif char == 'B' or char == 'R':
            minv = minv + (space / 2)

        if minv == maxv:
            return int(minv) - 1

    raise ValueError


def seat_id(desc):
    return binary_space_num(desc[:7], 128) * 8 + binary_space_num(desc[7:10], 8)


def part1():
    return max(map(seat_id, inp))


def part2():
    seats = sorted(list(map(seat_id, inp)))
    res = -1
    for idx in range(min(seats), max(seats) + 1):
        if idx not in seats:
            res = idx
    return res


# 913
print(part1())
# not 4, not 8
print(part2())
