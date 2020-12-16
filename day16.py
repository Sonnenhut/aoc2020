from functools import reduce


def parse_tickets(block):
    res = block.splitlines()[1:]
    res = list(map(lambda line: list(map(int, line.split(','))), res))
    return res


def parse_rules(blocks):
    res = {}
    for line in blocks[0].splitlines():
        name, rules_str = line.split(": ")
        res[name] = list(map(str_to_range, rules_str.split(" or ")))

    return res


def str_to_range(text):
    frompart, topart = text.split("-")
    return range(int(frompart), int(topart) + 1)


def parse_nearby_tickets(blocks):
    nearby_tickets = parse_tickets(blocks[2])

    invalid_fields = []
    res = []
    rule_values = parse_rules(blocks).values()
    for ticket in nearby_tickets:
        valid_ticket_fields = set()
        for rule in rule_values:
            valid_ticket_fields |= set(calc_valid_ticket_parts(ticket, rule))

        invalid_fields += set(ticket).difference(valid_ticket_fields)
        if set(ticket) == valid_ticket_fields:
            res.append(ticket)

    return res, invalid_fields


def calc_invalid_ticket_parts(ticket, rule_ranges):
    res = []

    for ticketpart in ticket:
        if 0 == sum(map(lambda rulepart: ticketpart in rulepart, rule_ranges)):
            res.append(ticketpart)
    return res


def calc_valid_ticket_parts(ticket, rule_ranges):
    res = []

    for ticketpart in ticket:
        if sum(map(lambda rulepart: ticketpart in rulepart, rule_ranges)) > 0:
            res.append(ticketpart)
    return res


def part1():
    blocks = open("inputs/day16.txt").read().split("\n\n")
    _, invalid_fields = parse_nearby_tickets(blocks)
    return sum(invalid_fields)


def part2():
    blocks = open("inputs/day16.txt").read().split("\n\n")
    rules = parse_rules(blocks)
    field_indices = {key: [] for key in rules.keys()}
    nearby_tickets, _ = parse_nearby_tickets(blocks)
    my_ticket = parse_tickets(blocks[1])[0]

    for rule_name in rules.keys():
        rule = rules[rule_name]
        for idx in range(len(my_ticket)):
            all_valid_for_idx = 1
            for ticket in nearby_tickets:
                ticket_part = ticket[idx:idx+1]
                all_valid_for_idx &= len(calc_valid_ticket_parts(ticket_part, rule))

            if all_valid_for_idx:
                field_indices[rule_name] += [idx]

    index = shorten_field_indices(field_indices)
    index = {key: index[key] for key in index.keys() if "departure" in key}
    return reduce(lambda acc, name: acc * my_ticket[index[name]], index.keys(), 1)


def shorten_field_indices(init_mapping):
    remaining = {key: set(init_mapping[key]) for key in init_mapping.keys()}
    res = {}
    while len(res) != len(init_mapping):
        fieldname = [key for key in remaining.keys() if len(remaining[key]) == 1][0]
        assigned_value = [*remaining.pop(fieldname)][0]
        res[fieldname] = assigned_value
        for values in remaining.values():
            values.remove(assigned_value)

    return res


# 23036
print(part1())
# 1909224687553
print(part2())
