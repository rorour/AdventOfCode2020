data = []

with open('day3_input.txt', mode='r') as infile:
    for line in infile:
        data += [line]


def calculate_trees(right, down=1):
    x = 0
    trees = 0
    line_num = 0
    try:
        while line_num < len(data):
            line_num += down
            if 0 < line_num < len(data):
                x = (x + right) % 31
                tree = data[line_num][x]
                if tree == '#':
                    trees += 1
        print(f'right {right} down {down} trees = {trees}')
    except IndexError:
        print(f'tried to access data[{line_num}][{x}]')
        return 0
    return trees


a = calculate_trees(1, 2)

total = calculate_trees(1) * calculate_trees(3) * calculate_trees(5) * calculate_trees(7) * calculate_trees(1, 2)
print(f'total is {total}')
