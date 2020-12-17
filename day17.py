import itertools
import sys


def solve(part=1):
    inp = open("inputs/day17.txt").read().splitlines()
    world = {(x, y, 0, 0): 1 for y in range(len(inp)) for x in range(len(inp[0])) if inp[y][x] == '#'}

    skip_4d = False
    if part == 1:
        skip_4d = True
    for _ in range(6):
        world = cycle(world, skip_4d)
    return len(world)


def all_locations(tuples, skip_4d=False):
    maxv = [-sys.maxsize, -sys.maxsize, -sys.maxsize, -sys.maxsize]
    minv = [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]

    for tpl in tuples:
        minv[0] = min(tpl[0], minv[0])
        minv[1] = min(tpl[1], minv[1])
        minv[2] = min(tpl[2], minv[2])
        minv[3] = min(tpl[3], minv[3])

        maxv[0] = max(tpl[0], maxv[0])
        maxv[1] = max(tpl[1], maxv[1])
        maxv[2] = max(tpl[2], maxv[2])
        maxv[3] = max(tpl[3], maxv[3])

    ranges = [range(minv[0] - 1, maxv[0] + 2), range(minv[1] - 1, maxv[1] + 2), range(minv[2] - 1, maxv[2] + 2)]
    if skip_4d:
        ranges.append([0])
    else:
        ranges.append(range(minv[3] - 1, maxv[3] + 2))
    return itertools.product(*ranges)


def cycle(world, skip_4d=False):
    res = {}
    for x, y, z, w in all_locations(world.keys(), skip_4d):
        cnt = active_neighbors((x, y, z, w), world)
        if cnt == 3 or (cnt == 2 and world.get((x, y, z, w), 0) == 1):
            res[(x, y, z, w)] = 1
    return res


def active_neighbors(initial, world, skip_4d=False):
    around_axis = [-1, 0, 1]
    around_axis4d = around_axis
    if skip_4d:
        around_axis4d = [0]
    res = 0
    for off_loc in itertools.product(around_axis, around_axis, around_axis, around_axis4d):
        if off_loc != (0, 0, 0, 0):
            search = tuple(map(sum, zip(initial, off_loc)))
            res += world.get(search, 0)
    return res


# 291
print(solve(1))
# 1524
print(solve(2))
