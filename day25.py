from itertools import islice


def public_keys(subj):
    res = 1
    while True:
        res *= subj
        res = res % 20201227
        yield res


def find_loop_size(challenge):
    res = -1
    for loop, num in enumerate(public_keys(7), 1):
        res = loop
        if num == challenge:
            break
    return res


def encryption_key(pub1, pub2):
    loop1 = find_loop_size(pub1)
    return next(islice(public_keys(pub2), loop1 - 1, None))


public1, public2 = open("inputs/day25.txt").read().splitlines()
public1, public2 = int(public1), int(public2)
print(encryption_key(public1, public2))
