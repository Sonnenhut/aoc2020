def part1():
    raw_lines = open("inputs/day21.txt").read().splitlines()
    without_allergens, _ = solve_allergens(raw_lines)
    return len(without_allergens)


def part2():
    lines = open("inputs/day21.txt").read().splitlines()
    _, allergen_causes = solve_allergens(lines)
    return ",".join(map(lambda key: next(iter(allergen_causes[key])), sorted(allergen_causes.keys())))


def solve_allergens(raw_lines):
    allergen_mapping = {}
    all_ingredients = []
    for raw_line in raw_lines:
        ingredients, allergens = raw_line.split(" (contains ")
        ingredients = set(ingredients.split(" "))
        all_ingredients += ingredients

        allergens = allergens.replace(")", "").split(", ")
        for allergen in allergens:
            allergen_mapping[allergen] = allergen_mapping.get(allergen, ingredients).intersection(ingredients)

    with_allergens = set(elem for allergen in allergen_mapping.values() for elem in allergen)
    without_allergens = list(filter(lambda ing: ing not in with_allergens, all_ingredients))

    allergen_causes = shorten_allergen_causes(allergen_mapping)

    return without_allergens, allergen_causes


def shorten_allergen_causes(allergen_mapping):
    res = {key: allergen_mapping[key].copy() for key in allergen_mapping.keys()}
    # until we know exactly which allergen can be mapped to one ingredient
    while len([i for i in res.values() if len(i) > 1]):
        single_ingredients = set(ing for ings in res.values() for ing in ings if len(ings) == 1)
        for allergen in res.keys():
            ingredients = res[allergen]
            if len(ingredients) > 1:
                res[allergen] = ingredients.difference(single_ingredients)
    return res


# 2125
print(part1())
# phc,spnd,zmsdzh,pdt,fqqcnm,lsgqf,rjc,lzvh
print(part2())
