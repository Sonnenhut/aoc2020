from functools import reduce

inp = [int(c) for c in open("inputs/day23.txt").read().splitlines()[0]]
#inp = [int(c) for c in "389125467"]


class Game:
    def __init__(self, arr):
        self.world = {}
        for key, value in zip(arr, arr[1:] + arr[0:1]):
            self.world[key] = value
        self.csr = arr[0]

    def tick(self):
        picked = self.take()
        dest = self.destination(picked)

        #print("taken", picked)
        #print("destination", dest)

        # slice out the taken bits
        self.world[self.csr] = self.world[picked[-1]]
        # and insert the taken between dest and clockwise to test
        self.world[dest], self.world[picked[-1]] = picked[0], self.world[dest]

        # destination becomes cursor
        self.csr = self.world[self.csr]

    def destination(self, ignore):
        i = self.csr - 1
        if i <= 0:
            i = max(self.world.keys())#self.end

        while True:
            if i not in ignore:
                break

            i -= 1
            if i <= 0:
                i = max(self.world.keys())
        return i

    def take(self):
        n1 = self.world[self.csr]
        n2 = self.world[n1]
        n3 = self.world[n2]
        return [n1, n2, n3]

    def labels_after_1(self, amt):
        res = []
        csr = 1
        while len(res) != amt:
            res += [self.world[csr]]
            csr = self.world[csr]
        return res

    def __str__(self):
        res = ["({})".format(self.csr)]
        csr = self.csr
        while len(res) != len(self.world.keys()):
            res += [str(self.world[csr])]
            csr = self.world[csr]
        return " ".join(res)


def part1():
    game = Game(inp)
    for i in range(100):
        game.tick()
    return "".join(str(i) for i in game.labels_after_1(len(inp) - 1))


def part2():
    inp_patched = inp + list(range(max(inp) + 1, 1_000_001))
    game = Game(inp_patched)
    for i in range(10_000_000):
        game.tick()
        if i % 1_000_000 == 0:
            print(i)

    return reduce(lambda acc, v: acc * v, game.labels_after_1(2))


# 43769582
print(part1())
# 264692662390
print(part2())
