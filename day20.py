from itertools import repeat, product
from operator import mul
from functools import reduce


def part1():
    tiles = parse_tile("inputs/day20t.txt")

    first_tile_num = next(iter(tiles.keys()))
    first_tile = tiles[first_tile_num]
    placed = {(0, 0): (first_tile_num, first_tile)}

    while len(placed) != len(tiles):
        to_add = {}
        already_placed_nums = list(map(lambda v: v[0], placed.values()))
        for placed_idx in placed.keys():
            _, placed_tile = placed[placed_idx]
            placed_x, placed_y = placed_idx

            for tile_num in tiles.keys():
                if tile_num in already_placed_nums:
                    continue
                tile = tiles[tile_num]
                off_x, off_y, tile_rot = place_tile(placed_tile, tile)
                if tile_rot is not None:
                    new_loc = (placed_x + off_x, placed_y + off_y)
                    to_add[new_loc] = tile_num, tile_rot
                    break
        placed |= to_add

    maxx = max(map(lambda loc: loc[0], placed.keys()))
    maxy = max(map(lambda loc: loc[1], placed.keys()))
    minx = min(map(lambda loc: loc[0], placed.keys()))
    miny = min(map(lambda loc: loc[1], placed.keys()))

    edge_nums = list(map(lambda loc: placed[loc][0], product([minx, maxx], [miny, maxy])))
    return reduce(mul, edge_nums)


def place_tile(fixtile, tile):
    stopx = len(fixtile[0])
    stopy = len(fixtile)

    north = list(zip(repeat(0), range(0, stopx)))
    south = list(zip(repeat(stopy - 1), range(0, stopx)))
    west = list(zip(range(0, stopy), repeat(0)))
    east = list(zip(range(0, stopy), repeat(stopx - 1)))

    fix_north = extract(fixtile, north)
    fix_south = extract(fixtile, south)
    fix_west = extract(fixtile, west)
    fix_east = extract(fixtile, east)

    res = 0, 0, None

    for tile_rot in orientations(tile):
        tile_rot_north = extract(tile_rot, north)
        tile_rot_south = extract(tile_rot, south)
        tile_rot_west = extract(tile_rot, west)
        tile_rot_east = extract(tile_rot, east)

        if fix_north == tile_rot_south:
            res = 0, -1, tile_rot
            break
        elif fix_south == tile_rot_north:
            res = 0, 1, tile_rot
            break
        elif fix_west == tile_rot_east:
            res = -1, 0, tile_rot
            break
        elif fix_east == tile_rot_west:
            res = 1, 0, tile_rot
            break
    return res


def extract(tile, locs):
    x = map(lambda l: l[1], locs)
    y = map(lambda l: l[0], locs)
    return list(map(at_loc, y, x, repeat(tile)))


def parse_tile(filename):
    res = {}
    blocks = open(filename).read().split("\n\n")
    for block in blocks:
        lines = block.splitlines()
        tile_id = int(lines[0].replace(":", "").replace("Tile ", ""))
        res[tile_id] = [list(iter(line)) for line in lines[1:]]
    return res


def orientations(tile):
    for amt in range(0, 4):
        yield rotate90cw(tile, amt)
        yield rotate90cw(flip(tile), amt)


def flip(tile):
    return tile[::-1]


def rotate90cw(tile, amt=1):
    if amt == 0:
        return tile
    else:
        res = [list(row) for row in zip(*tile[::-1])]
        return rotate90cw(res, amt - 1)


def at_loc(y, x, tile):
    return tile[y][x]


# 17148689442341
print(part1())
