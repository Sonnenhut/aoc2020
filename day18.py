from operator import mul, add
import re


def part1():
    terms = open("inputs/day18.txt").read().splitlines()
    return sum(map(lambda term: compute_recursive(term)[0], terms))


def part2():
    terms = open("inputs/day18.txt").read().splitlines()
    return sum(map(lambda term: eval(with_addition_paranthesis(term)), terms))


def with_addition_paranthesis(term):
    last_term = ""

    # add paranthesis around additions until we placed them all
    while last_term != term:
        last_term = term
        for m in re.finditer(r"\+", term):
            idx = m.start()
            start, stop = operand_idx(term, idx, -1), operand_idx(term, idx, 1) + 1
            replacement = "(" + term[start:stop] + ")"

            if replacement != term[max(start - 1, 0):min(stop + 1, len(term))]:
                term = term[0:start] + replacement + term[stop:]
                break
    return term


def extract_operation(term, operator_idx):
    idx = operator_idx
    return term[operand_idx(term, idx, -1): operand_idx(term, idx, 1) + 1]


def operand_idx(term, idx, off=1):
    brackets = 0
    while 0 <= idx < len(term):
        idx += off
        char = term[idx]
        if char == '(':
            brackets += off
        elif char == ')':
            brackets -= off
        elif char == ' ':
            continue

        if brackets == 0:
            break

    return idx


def compute_recursive(term, idx=0):
    acc = 0
    op = add
    while idx < len(term):
        char = term[idx]
        if char == "+":
            op = add
        elif char == "*":
            op = mul
        elif char.isdigit():
            acc = op(acc, int(char))
        elif char == '(':
            operand, idx = compute_recursive(term, idx + 1)
            acc = op(acc, operand)
        elif char == ')':
            break

        idx += 1

    return acc, idx


# 14006719520523
print(part1())
# 545115449981968
print(part2())
