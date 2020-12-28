def get_id(string: str):
    # first 7 are front/back (row)
    row_max = 127
    row_min = 0
    for i in range(0, 7):
        if string[i] == 'B':  # upper half
            row_min = ((row_max - row_min) // 2) + row_min + 1
        elif string[i] == 'F':  # lower half
            row_max = ((row_max - row_min) // 2) + row_min
        else:
            raise Exception(f'Unknown value {string[i]} for row')

    if row_min == row_max:
        print(f'Row is {row_min}')
    else:
        raise Exception('Row values not equal')

    # last 3 are left/right (column)
    col_min = 0
    col_max = 7
    for j in range(7, 10):
        if string[j] == 'L':  # lower half
            col_max = ((col_max - col_min) // 2) + col_min
        elif string[j] == 'R':  # upper half
            col_min = ((col_max - col_min) // 2) + col_min + 1
        else:
            raise Exception(f'Unknown value {string[j]} for col')
    if col_min == col_max:
        print(f'Col is {col_min}')
    else:
        raise Exception('Col values not equal')

    # print unique id
    seat_id = row_min * 8 + col_min
    print(f'id is {seat_id}')
    return seat_id


data = []
ids = []
with open('day5_input.txt', mode='r') as infile:
    for line in infile:
        data.append(line)

for line in data:
    ids.append(get_id(line))
    print(max(ids))

# part 2
for n in range(0, 992):
    if n not in ids:
        print(f'{n} not in ids')
