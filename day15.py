import sys

inp = list(map(int, open("inputs/day15.txt").read().replace("\n", "").split(",")))


def spoken_at_turn(wanted_turn):
    return next(x for i, x in enumerate(gen(inp), 1) if i == wanted_turn)


def part1():
    return spoken_at_turn(2020)


def part2():
    return spoken_at_turn(30000000)


def gen(initial):
    memory = {}
    for iturn, speak in enumerate(initial, 1):
        memory[speak] = iturn
        yield speak

    start_turn = len(initial) + 1
    spoken_last = initial[-1]
    for turn in range(start_turn, sys.maxsize):
        last_turn = turn - 1
        spoken_memory = memory.get(spoken_last, None)
        if spoken_memory is None or turn == start_turn:
            speak = 0
        else:
            speak = last_turn - spoken_memory

        yield speak

        memory[spoken_last] = last_turn
        spoken_last = speak


# 610
print(part1())
# 1407
print(part2())
