def initial_setup():
    data = []

    with open('day7_input.txt') as infile:
        for line in infile:
            data.append(line)

    data = [line.split(' bags contain ') for line in data]

    # for each line, [0] is bag color, [1] is numbers and colors of contained bags
    initial_bag_dict = {}
    for line in data:
        initial_bag_dict[line[0]] = line[1]
    return initial_bag_dict


def part_1_setup(initial_bag_dict: dict):
    bag_dict = {}  # this will store {contained color: [list of container colors]}
    # current format of i_b_d is {container color : string that lists contained colors}
    for container_color in initial_bag_dict.keys():  # initializing with all colors
        bag_dict[container_color] = []
    for container_color, contained_string in initial_bag_dict.items():
        # check if contains no other bags
        if contained_string == 'no other bags.\n':
            # do nothing
            # print(f'**{container_color} had no other bags')
            pass
        else:
            # split contained string into list of contained colors
            contained = contained_string.split(', ')
            # remove unnecessary characters
            contained = [x.replace('.', '') for x in contained]
            contained = [x.replace('\n', '') for x in contained]
            contained = [x.replace(' bags', '') for x in contained]
            contained = [x.replace(' bag', '') for x in contained]
            contained = [x[2:] for x in contained]

            # add container_color to each contained_color's list
            for color in contained:
                if color in bag_dict.keys():
                    bag_dict[color].append(container_color)
                else:
                    raise Exception(f'{color} not found in keys')

            # return map of {contained color : container color list}
    return bag_dict


def part_1_recursive(target_color: str, bag_dict: dict, outer_colors: list):
    if bag_dict[target_color] == []:
        return
    else:
        for contained_color in bag_dict[target_color]:
            if contained_color not in outer_colors:
                outer_colors.append(contained_color)
                part_1_recursive(contained_color, bag_dict, outer_colors)


def part_1():
    target_color = 'shiny gold'
    outer_colors = []
    initial_bag_dict = initial_setup()
    bag_dict = part_1_setup(initial_bag_dict)
    part_1_recursive(target_color, bag_dict, outer_colors)
    print(f'Part 1: {len(outer_colors)} colors')


def part_2_setup(initial_bag_dict: dict):
    bag_dict = {}  # this will store {container_color: [list with elements in form [num, color]]}
    # current format of i_b_d is {container color : string that lists contained colors}
    for container_color, contained_string in initial_bag_dict.items():
        bag_dict[container_color] = []
        # isolate numbers and colors
        if 'no other bags' in contained_string:
            # do nothing
            pass
        else:
            contained = contained_string.split(', ')
            # remove unnecessary characters
            contained = [x.replace('.', '') for x in contained]
            contained = [x.replace('\n', '') for x in contained]
            contained = [x.replace(' bags', '') for x in contained]
            contained = [x.replace(' bag', '') for x in contained]

            for num_color in contained:
                num_color = num_color.split(' ', 1)
                bag_dict[container_color].append([int(num_color[0]), num_color[1]])
    return bag_dict


def part_2_recursive(target_color: str, bag_dict: dict):
    if bag_dict[target_color] == []:
        return 0
    else:
        total = 0
        for num_color in bag_dict[target_color]:
            total_within_color = part_2_recursive(num_color[1], bag_dict)
            total += num_color[0] + total_within_color * num_color[0]
        return total


def part_2():
    target_color = 'shiny gold'
    total_bags = 0
    initial_bag_dict = initial_setup()
    bag_dict = part_2_setup(initial_bag_dict)
    total_bags = part_2_recursive(target_color, bag_dict)
    print(f'Part 2: {total_bags} bags')


# part_1()
part_2()
print('done')
