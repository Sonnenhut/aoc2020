import re


# Fake number which replaces matmul and pow operators to do addition with the side-effect that these operators
# have either the same or higher operator precedence than mul. This way python does all the logic for me.
# matmul (@) -> addition with same precedence as mul (*)
# exponentiation (**) -> addition with higher precedence as mul (*)
class FakeNum:
    def __init__(self, num):
        self.num = num

    def __mul__(self, other):
        return FakeNum(self.num * other.num)

    def __add__(self, other):
        return FakeNum(self.num + other.num)

    def __matmul__(self, other):
        return self + other

    def __pow__(self, power, modulo=None):
        return self + power

    def __str__(self):
        return "{}".format(self.num)


def part1():
    terms = open("inputs/day18.txt").read().splitlines()
    # replace + with @ which has same precedence as *
    terms = [re.sub(r"\+", r"@", term) for term in terms]
    terms = [re.sub(r"(\d)", r"FakeNum(\1)", term) for term in terms]
    return sum(map(eval, terms), FakeNum(0))


def part2():
    terms = open("inputs/day18.txt").read().splitlines()
    # replace + with ** which has same higher precedence as *
    terms = [re.sub(r"\+", r"**", term) for term in terms]
    terms = [re.sub(r"(\d)", r"FakeNum(\1)", term) for term in terms]
    return sum(map(eval, terms), FakeNum(0))


# 14006719520523
print(part1())
# 545115449981968
print(part2())
