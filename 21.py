import copy


class Food():
    def __init__(self):
        self.known_allergens = []
        self.ingredients = []


data = []
with open('day21_input.txt', 'r') as infile:
    for line in infile:
        data.append(line)

food = []
for line in data:
    line = line.split(' (contains ')
    new_food = Food()
    new_food.ingredients = line[0].split(' ')
    new_food.known_allergens = [x.strip(')\n') for x in line[1].split(', ')]
    food.append(new_food)

allergens = {}  # {allergen: [possible names]}
for f in food:
    for a in f.known_allergens:
        allergens[a] = []

# begin with possible names for allergen as all ingredients in foods w/ that listed allergen
for f in food:
    for a in f.known_allergens:
        for i in f.ingredients:
            if i not in allergens[a]:
                allergens[a].append(i)

# remove possible names which are not ingredients in other food w/known allergen
for f in food:
    for a in f.known_allergens:
        poss_names = copy.deepcopy(allergens[a])
        for possible_name in allergens[a]:
            if possible_name not in f.ingredients:
                poss_names.remove(possible_name)
        allergens[a] = copy.deepcopy(poss_names)

all_ingredients = []
for f in food:
    for i in f.ingredients:
        if i not in all_ingredients:
            all_ingredients.append(i)

potential_allergens = []
for allergen, potential_names in allergens.items():
    for n in potential_names:
        if n not in potential_allergens:
            potential_allergens.append(n)

non_allergens = [i for i in all_ingredients if i not in potential_allergens]

total = 0
for f in food:
    for i in f.ingredients:
        if i in non_allergens:
            total += 1

print(total)

all_allergens_identified = False
while not all_allergens_identified:
    for allergen, potential_names in allergens.items():
        if len(potential_names) == 1:
            for a, p_n in allergens.items():
                if a != allergen and potential_names[0] in p_n:
                    p_n.remove(potential_names[0])

    all_allergens_identified = True
    for allergen, potential_names in allergens.items():
        if len(potential_names) != 1:
            all_allergens_identified = False
            break

allergen_names = [a for a in allergens.keys()]
allergen_names.sort()
output = ''
for a in allergen_names:
    output += allergens[a][0]
    output += ','
print(output[:-1])
