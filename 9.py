data = []
with open('day9_input.txt', 'r') as infile:
    for line in infile:
        data.append(line)


def find_addends(valid_addends: list, potential_sum: int):
    found_addends = False
    for num1 in range(len(valid_addends)):
        for num2 in range(num1, len(valid_addends)):
            if valid_addends[num1] + valid_addends[num2] == potential_sum:
                found_addends = True
                # print(f'{potential_sum} is sum of {valid_addends[num1]} and {valid_addends[num2]}')
    return found_addends


def part_1():
    valid_addends = []
    preamble_size = 25
    for i in range(preamble_size):  # load preamble into valid addends
        valid_addends.append(int(data[i]))

    for j in range(preamble_size, len(data)):
        potential_sum = int(data[j])
        if not find_addends(valid_addends, potential_sum):
            print(f'{potential_sum} is not valid sum')
            return potential_sum
        else:  # update valid addends
            valid_addends.pop(0)
            valid_addends.append(potential_sum)
    return 0


def part_2(target: int):
    # define sequence with lower bound and upper bound
    for lower_index in range(len(data) - 1):  # subtract 1 bc sequence must be at least 2 numbers
        upper_index = lower_index + 1

        lower_val = int(data[lower_index])

        sum = lower_val
        sequence = [lower_val]
        while upper_index < len(data) and sum < target:
            upper_val = int(data[upper_index])
            sequence.append(upper_val)
            sum += upper_val
            if sum == target:
                print(f'found sum in {sequence}')
                return sequence
            else:
                upper_index += 1



invalid_sum = part_1()
sequence = part_2(invalid_sum)
print(max(sequence) + min(sequence))
