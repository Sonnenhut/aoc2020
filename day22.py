def part1():
    decks = open("inputs/day22.txt").read().split("\n\n")
    decks = [list(map(int, deck.splitlines()[1:])) for deck in decks]

    deck1, deck2 = decks
    score1, score2 = combat(deck1, deck2)
    return max(score1, score2)


def part2():
    decks = open("inputs/day22.txt").read().split("\n\n")
    decks = [list(map(int, deck.splitlines()[1:])) for deck in decks]

    deck1, deck2 = decks
    score1, score2 = recursive_combat(deck1, deck2)
    return max(score1, score2)


def combat(deck1, deck2):
    while len(deck1) and len(deck2):
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

    return score(deck1), score(deck2)


def recursive_combat(deck1, deck2):
    played_rounds = set()
    while len(deck1) and len(deck2):
        memory = (tuple(deck1), tuple(deck2))
        # player 1 wins if this exact round was already played...
        if memory in played_rounds:
            deck1, deck2 = [1], [0]
            break
        else:
            played_rounds.add(memory)

        card1, card2 = deck1.pop(0), deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            score1, score2 = recursive_combat(deck1[:card1], deck2[:card2])
            diff = score1 - score2
        else:
            diff = card1 - card2

        if diff > 0:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

    return score(deck1), score(deck2)


def score(deck):
    return sum(map(mulpair, enumerate(reversed(deck), 1)))


def mulpair(p):
    return p[0] * p[1]


# 32629
print(part1())
# 32519
print(part2())
