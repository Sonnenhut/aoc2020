def part1():
    return len(parse_black_tiles("inputs/day24.txt"))


def part2():
    blacks = parse_black_tiles("inputs/day24.txt")

    for _ in range(100):
        new_blacks = blacks.copy()
        adjacent_whites = {}
        for x, y in blacks:
            adjacent = set(map(lambda d: move(x, y, d), ["ne", "nw", "se", "sw", "w", "e"]))
            adjacent_black_cnt = len(blacks.intersection(adjacent))

            if adjacent_black_cnt == 0 or adjacent_black_cnt > 2:
                new_blacks.remove((x, y))

            # remember that all white adjacent ones have one black adjacent tile
            for white_coord in adjacent.difference(blacks):
                adjacent_whites[white_coord] = adjacent_whites.get(white_coord, 0) + 1

        white_turn_black = {coord for coord in adjacent_whites if adjacent_whites[coord] == 2}
        blacks = new_blacks | white_turn_black
    return len(blacks)


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


# odd-r layout https://www.redblobgames.com/grids/hexagons/#coordinates
def move(x, y, directions):
    if len(directions) == 0:
        return x, y
    d, rest = directions[0], directions[1:]
    if d in ["n", "s"]:
        d, rest = directions[:2], directions[2:]

    # odd-r layout of a hexagon
    odd = y % 2
    even = 1 - odd

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
