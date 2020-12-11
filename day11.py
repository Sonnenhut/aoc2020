import itertools


def parse_input(file_name):
    return open(file_name, "r").read().splitlines()


def cycle(state, calc):
    new_state = []
    for y in range(len(state)):
        new_state.append([calc(x, y, state) for x in range(len(state[y]))])
    return new_state


def calc_seat_part1(x, y, state):
    curr = state[y][x]
    res = curr

    if curr == 'L' and adjacent_occupied(x, y, 1, state) == 0:
        res = '#'
    elif curr == '#' and adjacent_occupied(x, y, 4, state) >= 4:
        res = 'L'
    return res


def adjacent_occupied(x, y, desired_occupied, state):
    res = 0
    maxx = len(state[0])
    maxy = len(state)

    for pos_x, pos_y in itertools.product(range(x - 1, x + 2), range(y - 1, y + 2)):
        if pos_y < 0 or pos_x < 0 or pos_y >= maxy or pos_x >= maxx:
            continue
        elif state[pos_y][pos_x] == '#' and (pos_x, pos_y) != (x, y):
            res += 1
            if res == desired_occupied:
                break
    return res


def part1():
    state = parse_input("inputs/day11.txt")
    prev_state = []
    while state != prev_state:
        prev_state = state
        state = cycle(state, calc_seat_part1)
    return sum([line.count('#') for line in state])


def part2():
    state = parse_input("inputs/day11.txt")
    prev_state = []
    while state != prev_state:
        prev_state = state
        state = cycle(state, calc_seat_part2)
    return sum([line.count('#') for line in state])


def calc_seat_part2(x, y, state):
    curr = state[y][x]
    res = curr

    if curr == 'L' and visible_occupied(x, y, 1, state) == 0:
        res = '#'
    elif curr == '#' and visible_occupied(x, y, 5, state) >= 5:
        res = 'L'
    return res


def visible_occupied(x, y, desired_occupied, state):
    minx = 0
    stopx = len(state[0])
    miny = 0
    stopy = len(state)

    up_y = list(reversed(range(miny, y)))
    down_y = list(range(y + 1, stopy))
    left_x = list(reversed(range(minx, x)))
    right_x = list(range(x + 1, stopx))

    directions = [
        zip(itertools.repeat(x), up_y),
        zip(itertools.repeat(x), down_y),
        zip(left_x, itertools.repeat(y)),
        zip(right_x, itertools.repeat(y)),
        zip(left_x, up_y),
        zip(right_x, up_y),
        zip(left_x, down_y),
        zip(right_x, down_y),
    ]

    res = 0
    for direction in directions:
        for pos_x, pos_y in direction:
            char = state[pos_y][pos_x]
            if '.' == char:
                continue
            elif 'L' == char:
                break
            elif '#' == char:
                res += 1
                if res == desired_occupied:
                    return res
                else:
                    break
    return res


# 2310
print(part1())
# 2074
print(part2())
