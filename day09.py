from itertools import combinations


def parse_input(file_name):
    return list(map(int, open(file_name, "r").read().splitlines()))


def part1(off=25):
    seq = parse_input("inputs/day09.txt")
    check = seq[:off]
    for idx, num in enumerate(seq[off:], off):
        if num not in map(sum, combinations(check, 2)):
            return num
        check = seq[idx-off+1:idx+1]
    return -1


def part2():
    challenge = part1()
    seq = parse_input("inputs/day09.txt")
    for csr_start in range(0, len(seq)):
        moving_sum = seq[csr_start]
        for csr_end in range(csr_start+1, len(seq)):
            moving_sum += seq[csr_end]
            if moving_sum > challenge:
                break
            elif moving_sum == challenge:
                window = seq[csr_start:csr_end+1]
                return min(window) + max(window)
    return -1


# 90433990
print(part1())
# 11691646
print(part2())
