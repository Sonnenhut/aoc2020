import sys
from operator import sub


inp = list(map(int, "9,12,1,4,17,0,18".split(",")))


def spoken_at_turn(wanted_turn):
    res = -1
    for turn, spoken in enumerate(gen(inp), 1):
        if turn == wanted_turn:
            res = spoken
            break

    return res


def part1():
    return spoken_at_turn(2020)


def part2():
    return spoken_at_turn(30000000)


def gen(initial):
    memory = {}
    for iturn, speak in enumerate(initial, 1):
        memory[speak] = (iturn, 0)
        yield speak

    last = initial[-1]
    for turn in range(len(initial) + 1, sys.maxsize):
        last_spoken_at = memory.get(last, (0, 0))
        if 0 in last_spoken_at:
            speak = 0
        else:
            speak = sub(*last_spoken_at)

        last_turn, before_turn = memory.get(speak, (0, 0))
        memory[speak] = (turn, last_turn)
        last = speak
        yield speak


# 610
print(part1())
# 1407
print(part2())
