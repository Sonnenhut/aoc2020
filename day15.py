import sys
import itertools

inp = list(map(int, open("inputs/day15.txt").read().replace("\n", "").split(",")))


def spoken_at_turn(wanted_turn):
    return next(itertools.islice(gen(inp), wanted_turn - 1, None))


def gen(initial):
    memory = [-1] * 30000000
    for iturn, speak in enumerate(initial, 1):
        memory[speak] = iturn
        yield speak

    start_turn = len(initial) + 1
    spoken_last = initial[-1]
    for turn in range(start_turn, sys.maxsize):
        last_turn = turn - 1
        spoken_memory = memory[spoken_last]
        if spoken_memory == -1:
            speak = 0
        else:
            speak = last_turn - spoken_memory

        yield speak

        memory[spoken_last] = last_turn
        spoken_last = speak


# part1_ 610
print(spoken_at_turn(2020))
# part2: 1407
print(spoken_at_turn(30000000))
