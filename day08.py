def _line_split(line):
    op, arg = line.split(" ")
    return op, int(arg)


class InfiniteLoopError(Exception):
    pass


class Pgm(object):
    def __init__(self, lines):
        self.csr_hist = []
        self.instr = list(map(_line_split, lines))
        self.csr = 0
        self.acc_value = 0

    def acc(self, arg):
        self.acc_value += arg
        self.csr += 1

    def nop(self, arg):
        self.csr += 1

    def jmp(self, arg):
        self.csr += arg

    def exec_next(self):
        self.csr_hist.append(self.csr)

        op, arg = self.instr[self.csr]
        getattr(self, op)(arg)

        return self.csr

    def exec_until_infinite_loop(self):
        res = -1
        try:
            self.exec()
        except InfiniteLoopError:
            res = self.acc_value
        return res

    def exec(self):
        while True:
            if self.csr in self.csr_hist:
                raise InfiniteLoopError
            if self.csr == len(self.instr):
                # pgm exited nicely
                break
            self.exec_next()

        return self.acc_value


def part1():
    pgm = Pgm(open("inputs/day08.txt").read().splitlines())
    return pgm.exec_until_infinite_loop()


def input_mutations(input_lines):
    for idx, line in enumerate(input_lines):
        if "nop" in line:
            mutation = input_lines.copy()
            mutation[idx] = line.replace("nop", "jmp")
            yield mutation
        if "jmp" in line:
            mutation = input_lines.copy()
            mutation[idx] = line.replace("jmp", "nop")
            yield mutation


def part2():
    res = -1
    # try out all mutations of jmp -> nop / nop -> jmp
    for mutation in input_mutations(open("inputs/day08.txt").read().splitlines()):
        try:
            res = Pgm(mutation).exec()
        except InfiniteLoopError:
            pass
    return res


# 1915
print(part1())
# 944
print(part2())
