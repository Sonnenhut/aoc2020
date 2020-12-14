import math


def part1():
    off, buses = open("inputs/day13.txt").read().splitlines()
    off, buses = int(off), map(int, filter(lambda x: x != 'x', buses.split(",")))

    res = min([(bus - (off % bus), bus) for bus in buses])
    return res[0] * res[1]


# https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset
# By Euclid's Lemma there exists integers M,N so that M∗Red−N∗Green=a.
# Find those and have Red and Green take those steps to get a number they will be synched at.
# --> *** Then all multiples of the LCM from there will have them in synch. ***
def part2():
    _, buses = open("inputs/day13.txt").read().splitlines()
    buses = buses.split(",")

    sorted_buses = filter(lambda b: b != 'x', buses)
    sorted_buses = list(map(lambda bus: (int(bus), buses.index(bus)), sorted_buses))

    increase, _ = sorted_buses[0]
    curr = 0

    for stop in range(2, len(sorted_buses) + 1):
        view = sorted_buses[:stop]

        # find the time where some of the buses meet
        curr = increase_until_buses_meet(curr, increase, view)

        # found the time where the buses meet, from there on, these buses will meet at that point + multiple of lcm
        increase = math.lcm(*[pair[0] for pair in view])

    return curr


def increase_until_buses_meet(start, step, buses):
    curr = start + step
    offset_to_wanted = -1
    while offset_to_wanted != 0:
        curr += step

        offset_to_wanted = 0
        for bus, bus_offset in buses:
            # is the bus in the correct place?
            offset_to_wanted += (curr + bus_offset) % bus
            if offset_to_wanted > 0:
                break

    return curr


# 2845
print(part1())
# 487905974205117
print(part2())
