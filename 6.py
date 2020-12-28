data = []

with open('day6_input.txt') as infile:
    for line in infile:
        data.append(line)

data = [x.strip('\n') for x in data]  # strip newlines from data


def part_one():
    i = 0
    total = 0
    while i < len(data):  # go through all lines in file
        questions = []  # create new list for group
        while i < len(data) and len(data[i]) > 0:  # for each valid line in group
            for q in data[i]:
                if q not in questions:
                    questions.append(q)
            i += 1
        # finished with group
        group_sum = len(questions)
        print(f'group had {group_sum}')
        total += group_sum
        i += 1
    return total


def part_two():
    i = 0
    total = 0
    while i < len(data):  # go through all lines in file
        questions = [a for a in data[i]]  # create new list for group
        while i < len(data) and len(data[i]) > 0:  # for each valid line in group
            questions = [q for q in questions if q in data[i]]
            i += 1
        # finished with group
        group_sum = len(questions)
        print(f'group had {group_sum}')
        total += group_sum
        i += 1
    return total


print(f'total is {part_two()}')
