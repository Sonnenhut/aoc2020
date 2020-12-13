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
    sorted_buses = map(lambda b: (b, buses.index(b)), sorted_buses)
    sorted_buses = list(reversed(sorted(map(lambda pair: (int(pair[0]), pair[1]), sorted_buses))))

    big_buses = sorted_buses[:4]
    # find a relatively high point where big numbers match the criteria
    curr = increase_until_buses_meet(0, *big_buses[0], big_buses)

    # from that matching point onwards all of the next "meeting points" will be in steps of the lcm
    # happily enough the lcm will be huge, as we do this step for the big bus numbers
    increase = math.lcm(*[pair[0] for pair in big_buses])

    # from the point where some (big) numbers match the criteria go in big increase steps and search for a lucky match
    curr_base = increase_until_buses_meet(curr, increase, 0, sorted_buses)

    return curr_base


def increase_until_buses_meet(start, step, step_offset, buses):
    curr = start + step
    curr_base = curr - step_offset
    offset_to_wanted = -1
    while offset_to_wanted != 0:
        curr += step
        curr_base = curr - step_offset

        offset_to_wanted = 0
        for bus, bus_offset in buses:
            # is the bus in the correct place?
            offset_to_wanted += (curr_base + bus_offset) % bus
            if offset_to_wanted > 0:
                break

    return curr_base


# 2845
print(part1())
# 487905974205117
print(part2())
