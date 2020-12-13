def part1():
    instructions = open("inputs/day12.txt").read().splitlines()
    x, y = (0, 0)
    facing = 'E'
    for instruction in instructions:
        facing, offx, offy = apply_instruction_pt1(facing, instruction)
        x += offx
        y += offy
    return abs(x) + abs(y)


def apply_instruction_pt1(facing, instruction):
    directions = ['N', 'E', 'S', 'W'] * 2
    action = instruction[:1]
    value = int(instruction[1:])

    x, y = (0, 0)
    if action == 'N':
        y -= value
    elif action == 'S':
        y += value
    elif action == 'W':
        x -= value
    elif action == 'E':
        x += value
    elif action == 'R':
        idx = directions.index(facing)
        facing = directions[idx + int(value / 90)]
    elif action == 'L':
        idx = directions.index(facing)
        facing = directions[idx + int(-value / 90)]
    elif action == 'F':
        facing, x, y = apply_instruction_pt1(facing, "{}{}".format(facing, value))
    return facing, x, y


def part2():
    instructions = open("inputs/day12.txt").read().splitlines()
    wp_x, wp_y = (10, -1)
    x, y = (0, 0)
    for instruction in instructions:
        wp_x, wp_y, offx, offy = apply_instruction_pt2((wp_x, wp_y), instruction)
        x += offx
        y += offy
    return abs(x) + abs(y)


def apply_instruction_pt2(waypoint, instruction):
    wp_x, wp_y = waypoint

    action = instruction[:1]
    value = int(instruction[1:])

    x, y = (0, 0)
    if action == 'N':
        wp_y -= value
    elif action == 'S':
        wp_y += value
    elif action == 'W':
        wp_x -= value
    elif action == 'E':
        wp_x += value
    elif action == 'R' or action == 'L':
        wp_x, wp_y = rotate(instruction, (wp_x, wp_y))
    elif action == 'F':
        x += value * wp_x
        y += value * wp_y

    return wp_x, wp_y, x, y


def rotate(instruction, position):
    x, y = position
    action = instruction[:1]
    value = int(instruction[1:])

    if action == 'R':
        times = value / 90
        for _ in range(int(times)):
            x, y = -y, x
    elif action == 'L':
        times = (360 - value) / 90
        for _ in range(int(times)):
            x, y = -y, x
    return x, y


# 439
print(part1())
# 12385
print(part2())
