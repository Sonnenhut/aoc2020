from functools import reduce


def part1():
    return len(parse_black_tiles("inputs/day24.txt"))


def part2():
    blacks = parse_black_tiles("inputs/day24.txt")

    for i in range(100):
        tiles = reduce(lambda acc, p: acc | adjacent_coords(*p), blacks, blacks)
        new_blacks = blacks.copy()
        for x, y in tiles:
            adjacent = adjacent_coords(x, y)
            adjacent_black_cnt = len(blacks.intersection(adjacent))
            if (x, y) in blacks:
                if adjacent_black_cnt == 0 or adjacent_black_cnt > 2:
                    new_blacks.remove((x, y))
            else:
                if adjacent_black_cnt == 2:
                    new_blacks.add((x, y))
        blacks = new_blacks
    return len(blacks)


def adjacent_coords(x, y):
    return set(map(lambda d: move(x, y, d), ["ne", "nw", "se", "sw", "w", "e"]))


def parse_black_tiles(filename):
    lines = open(filename).read().splitlines()

    res = set()
    for line in lines:
        turn = move(0, 0, line)
        if turn in res:
            res.remove(turn)
        else:
            res.add(turn)
    return res


#odd-r layout
def move(x, y, directions):
    if len(directions) == 0:
        return x, y
    d, rest = directions[0], directions[1:]
    if d in ["n", "s"]:
        d, rest = directions[:2], directions[2:]

    # odd-r layout of a hexagon
    if y % 2 == 0:
        even = 1
        odd = 0
    else:
        even = 0
        odd = 1

    if d == "nw":
        x, y = x - even, y - 1
    elif d == "ne":
        x, y = x + odd, y - 1
    elif d == "sw":
        x, y = x - even, y + 1
    elif d == "se":
        x, y = x + odd, y + 1
    elif d == "w":
        x -= 1
    elif d == "e":
        x += 1

    return move(x, y, rest)


# 287
print(part1())
# 3636
print(part2())
