input = open("inputs/day02.txt", "r").read().splitlines()


def part1():
    cnt = 0
    for line in input:
        line = line.replace("\n", "")
        [desc, pw] = line.split(": ")
        [amount, char] = desc.split(" ")
        [minv, maxv] = amount.split("-")

        if int(maxv) >= pw.count(char) >= int(minv):
            cnt += 1
    return cnt


def part2():
    cnt = 0
    for line in input:
        line = line.replace("\n", "")
        [desc, pw] = line.split(": ")
        [amount, char] = desc.split(" ")
        [pos1, pos2] = amount.split("-")
        if (pw[int(pos1) - 1] == char) != (pw[int(pos2) - 1] == char):
            cnt += 1
    return cnt


# 582
print(part1())
# 729
print(part2())
