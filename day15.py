import sys
from operator import sub

inp = list(map(int, "9,12,1,4,17,0,18".split(",")))


def spoken_at_turn(wanted_turn):
    return next(x for i, x in enumerate(gen(inp), 1) if i == wanted_turn)


def part1():
    return spoken_at_turn(2020)


def part2():
    return spoken_at_turn(30000000)


def gen(initial):
    memory = {}
    for iturn, speak in enumerate(initial, 1):
        memory[speak] = (iturn, 0)
        yield speak

    spoken_at = memory[initial[-1]]
    for turn in range(len(initial) + 1, sys.maxsize):
        if 0 in spoken_at:
            speak = 0
        else:
            speak = sub(*spoken_at)

        last_turn, _ = memory.get(speak, (0, 0))
        spoken_at = (turn, last_turn)
        memory[speak] = spoken_at

        yield speak


# 610
print(part1())
# 1407
print(part2())
