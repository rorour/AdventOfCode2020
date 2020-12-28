def part_one(mn, mx, val, pw):
    valid = 0
    char_count = 0
    for x in pw:
        if x == val:
            char_count += 1

    if char_count >= mn and char_count <= mx:
        valid += 1

    return valid


def part_two(pos1, pos2, val, pw):
    try:
        found = 0
        if pw[pos1 - 1] == val:  # add one because index 0 is position 1
            found += 1
        if pw[pos2 - 1] == val:
            found += 1
        if found == 1:
            return 1
        else:
            return 0
    except IndexError:
        print(f'tried to access index {pos1 + 1} and {pos2 + 1} in string {pw} of length {len(pw)}')


# main #################################################################
data = []
with open('day2_input.txt', mode='r') as infile:
    for line in infile:
        data += [line]

# split data into 4 parts: min, max, val, and password:
valid = 0
for line in data:
    vals = line.split(' ')
    minmax = vals[0].split('-')

    mn = int(minmax[0])
    mx = int(minmax[1])
    val = vals[1].split(':')[0]
    pw = vals[2].split('\n')[0]
    # print(f'min is {mn} max is {mx} val is {val} pw is {pw}')

    # valid += part_one(mn, mx, val, pw)
    valid += part_two(mn, mx, val, pw)

print(f'{valid} valid passwords.')
