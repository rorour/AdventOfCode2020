def part_1(data):
    differences = {}
    for i in range(len(data) - 1):
        diff = data[i + 1] - data[i]
        if diff not in differences:
            differences[diff] = 1
        else:
            differences[diff] += 1
    print(differences)
    print(f'there are {differences[1]} 1-diffs and {differences[3]} 3-diffs')


def positive_factorial(x: int):
    if x > 1:
        return x * positive_factorial(x - 1)
    else:
        return 1


def n_choose_r(n: int, r: int):
    numerator = positive_factorial(n)
    denominator = positive_factorial(r) * positive_factorial(n - r)
    return int(numerator / denominator)


def part_2(data):
    # differences exist when 2 joltages with a diff of 3 have other joltages between them.
    total_options = 1
    taken_max = []
    taken_min = []
    for i in range(len(data) - 1):
        break_j = False
        for j in range(i + 1, len(data) - 1):
            val1 = data[i]
            val2 = data[j]
            if (j - i == 1 and val2 - val1 >= 3) or (val2 - data[j - 1] > 1):
                break_j = True
            if not break_j and data[j+1] - data[j] == 3 and data[j] - data[i] > 1 and j - i > 1 and val2 not in taken_max and val1 not in taken_min:
                break_j = True
                x = j - i - 1
                options = 0
                for y in range(x + 1):
                    options += n_choose_r(x, y)
                if val2 - val1 > 3:
                    subtract_options = int((val2 - val1) / 3)
                    print(f'subtracted {subtract_options}')
                    options -= subtract_options


                print(f'{val1} and {val2} have {options} options between them. x is {x}')
                total_options *= options
                taken_max.append(val2)
                for n in range(i, j):
                    taken_min.append(data[n])

    print(data)
    print(f'{total_options} total options')

data = []
with open('day10_input.txt', 'r') as infile:
    for line in infile:
        data.append(int(line))

outlet = 0
device = max(data) + 3
data.append(outlet)
data.append(device)
data.sort()

part_1(data)
part_2(data)
