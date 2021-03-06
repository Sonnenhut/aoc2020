from itertools import repeat, product
from operator import mul
from functools import reduce, cache
import re


def part1():
    tiles = parse_tile("inputs/day20.txt")
    placed = place_tiles(tiles)
    placed = {key: placed[key][0] for key in placed.keys()}

    maxx = max(map(lambda loc: loc[0], placed.keys()))
    maxy = max(map(lambda loc: loc[1], placed.keys()))
    minx = min(map(lambda loc: loc[0], placed.keys()))
    miny = min(map(lambda loc: loc[1], placed.keys()))

    edge_nums = list(map(lambda loc: placed[loc], product([minx, maxx], [miny, maxy])))
    return reduce(mul, edge_nums)


def part2():
    image = image_from_input("inputs/day20.txt")
    #                    #
    #  #    ##    ##    ###
    #   #  #  #  #  #  #
    monster_width = 20
    line_fill = "." * (len(image) - monster_width)
    rgx_str = r"(..................)(#)(." + line_fill
    rgx_str += ")(#)(....)(##)(....)(##)(....)(###)(" + line_fill
    rgx_str += ".)(#)(..)(#)(..)(#)(..)(#)(..)(#)(..)(#)(...)"

    monster_sub = r'\1O\3O\5OO\7OO\9OOO\11O\13O\15O\17O\19O\21O\23'
    monster_regex = re.compile(rgx_str)

    res = ""
    for image_rot in rotations(image):
        image_str = "".join([elem for line in image_rot for elem in line])
        res = exhaustive_sub(monster_regex, monster_sub, image_str)
        if image_str != res:
            break

    return reduce(lambda acc, l: acc + l.count('#'), res, 0)


def exhaustive_sub(regex, rgx_sub, image_str):
    res = image_str
    last = ""
    while last != res:
        last = res
        res = regex.sub(rgx_sub, res)

    return res


def image_from_input(filename):
    tiles = parse_tile(filename)
    placed = place_tiles(tiles)
    # remove the ids
    placed = {key: placed[key][1] for key in placed.keys()}

    # remove borders of each tile
    for key in placed.keys():
        placed[key] = tuple(line[1:-1] for line in placed[key])[1:-1]

    maxx = max(map(lambda loc: loc[0], placed.keys()))
    maxy = max(map(lambda loc: loc[1], placed.keys()))
    minx = min(map(lambda loc: loc[0], placed.keys()))
    miny = min(map(lambda loc: loc[1], placed.keys()))

    res = []
    for y in range(miny, maxy + 1):
        same_y_tiles = [placed[(x, y)] for x in range(minx, maxx + 1)]
        for line in append_rows(same_y_tiles):
            res.append(tuple(line))

    return tuple(res)


def append_rows(tiles):
    res = []
    for y in range(0, len(tiles[0])):
        line = []
        for tile in tiles:
            line += tile[y]
        res.append(line)
    return res


def place_tiles(tiles):
    first_tile_num = next(iter(tiles.keys()))
    first_tile = tiles[first_tile_num]
    res = {(0, 0): (first_tile_num, first_tile)}

    while len(res) != len(tiles):
        to_add = {}
        already_placed_nums = list(map(lambda v: v[0], res.values()))
        for placed_idx in res.keys():
            _, placed_tile = res[placed_idx]
            placed_x, placed_y = placed_idx

            for tile_num in tiles.keys():
                if tile_num in already_placed_nums:
                    continue
                tile = tiles[tile_num]
                off_x, off_y, tile_rot = lock_tile(placed_tile, tile)
                if tile_rot is not None:
                    new_loc = (placed_x + off_x, placed_y + off_y)
                    to_add[new_loc] = tile_num, tile_rot
                    break
        res |= to_add
    return res


@cache
def lock_tile(fixtile, tile):
    stopx = len(fixtile[0])
    stopy = len(fixtile)

    north = tuple(zip(repeat(0), range(0, stopx)))
    south = tuple(zip(repeat(stopy - 1), range(0, stopx)))
    west = tuple(zip(range(0, stopy), repeat(0)))
    east = tuple(zip(range(0, stopy), repeat(stopx - 1)))

    res = 0, 0, None

    for tile_rot in rotations(tile):
        if extract(fixtile, north) == extract(tile_rot, south):
            res = 0, -1, tile_rot
            break
        elif extract(fixtile, south) == extract(tile_rot, north):
            res = 0, 1, tile_rot
            break
        elif extract(fixtile, west) == extract(tile_rot, east):
            res = -1, 0, tile_rot
            break
        elif extract(fixtile, east) == extract(tile_rot, west):
            res = 1, 0, tile_rot
            break
    return res


@cache
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
        res[tile_id] = tuple(tuple(iter(line)) for line in lines[1:])
    return res


@cache
def rotations(tile):
    res = []
    flipped = tile[::-1]
    for amt in range(0, 4):
        res.append(rotate90cw(tile, amt))
        res.append(rotate90cw(flipped, amt))
    return res


def rotate90cw(tile, amt=1):
    if amt == 0:
        return tile
    else:
        res = tuple(t for t in zip(*tile[::-1]))
        return rotate90cw(res, amt - 1)


def at_loc(y, x, tile):
    return tile[y][x]


# 17148689442341
print(part1())
# 2009
print(part2())
