import itertools


def cycle(state, calc):
    new_state = []
    for y in range(len(state)):
        line = [calc(x, y, state) for x in range(len(state[y]))]
        new_state.append(line)
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
    state = open("inputs/day11.txt").read().splitlines()
    prev_state = []
    while state != prev_state:
        prev_state = state
        state = cycle(state, calc_seat_part1)
    return sum([line.count('#') for line in state])


def part2():
    state = open("inputs/day11.txt").read().splitlines()
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
    checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    res = 0
    for x_off, y_off in checks:
        vis = visible_in_direction(x, y, x_off, y_off, state)
        if 'L' == vis:
            continue
        elif '#' == vis:
            res += 1
            if res == desired_occupied:
                break
    return res


def visible_in_direction(x, y, x_off, y_off, state):
    pos_x = x + x_off
    pos_y = y + y_off
    res = '.'
    if 0 <= pos_x < len(state[0]) and 0 <= pos_y < len(state):
        char = state[pos_y][pos_x]
        if '#' == char or 'L' == char:
            res = char
        else:
            res = visible_in_direction(pos_x, pos_y, x_off, y_off, state)
    return res


# 2310
print(part1())
# 2074
print(part2())
