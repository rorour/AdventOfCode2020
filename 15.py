def part_1(turns, turns_to_take):
    for n in range(0, turns_to_take):
        last_num = turns[len(turns) - 1]
        last_index = len(turns) - 1
        new_num = None
        if last_num in turns[0:-1]:
            found_indices = [i for i, j in enumerate(turns[0:-1]) if j == last_num]
            previous_index = found_indices[len(found_indices) - 1]
            new_num = last_index - previous_index
        else:
            new_num = 0
        if new_num is not None:
            turns.append(new_num)

    for i, j in enumerate(turns):
        print(f'{i + 1}: {j}')


def part_2(turns, turns_to_take):
    turns_dict = {}  # key = num; val = (most recent index of num, frequency)
    # initialize turns dict
    for i, x in enumerate(turns):
        current_val = turns_dict.get(x, False)
        if current_val:
            turns_dict[x] = (current_val[0], current_val[1] + 1)
        else:
            turns_dict[x] = (i, 1)

    v = turns[len(turns) - 1]  # value of previous item
    for t in range(len(turns), turns_to_take):  # t = index in sequence of new val
        value_tuple = turns_dict.get(v, (None, 0))
        mri = value_tuple[0]  # most recent index of previous item
        f = value_tuple[1]  # frequency of previous item
        new_val = None  # the new item that will be said at index t
        if f > 0:  # new item is difference between previous 2 indexes
            new_val = (t - 1) - mri
            turns_dict[v] = (t - 1, f + 1)
        else:  # previous item was said for the first time
            new_val = 0
            turns_dict[v] = (t - 1, 1)  # add last value to dictionary
        v = new_val  # make current new val last val
        print(f'{t + 1}: {new_val}')


turns = [0,13,1,8,6,15]
turns_to_take = 30000000
part_2(turns, turns_to_take)
