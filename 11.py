import copy


def initialize(data):
    with open('day11_input.txt', 'r') as infile:
        for line in infile:
            row = []
            for spot in line:
                if not spot == '\n':
                    row.append(spot)
            data.append(row)


def seat_iteration(data):
    changed_seats = False
    new_data = copy.deepcopy(data)
    for r in range(len(data)):
        row = data[r]
        for c in range(len(row)):

            adjacent = {'L': 0, '#': 0, '.': 0}
            if not r == 0:
                if not c == 0:
                    adjacent[data[r - 1][c - 1]] += 1  # top left
                adjacent[data[r - 1][c]] += 1  # top middle
                if not c == len(row) - 1:
                    adjacent[data[r - 1][c + 1]] += 1  # top right
            if not c == 0:
                adjacent[data[r][c - 1]] += 1  # middle left
                if not r == len(data) - 1:
                    adjacent[data[r + 1][c - 1]] += 1  # bottom left
            if not c == len(row) - 1:
                adjacent[data[r][c + 1]] += 1  # middle right
                if not r == len(data) - 1:
                    adjacent[data[r + 1][c + 1]] += 1  # bottom right
            if not r == len(data) - 1:
                adjacent[data[r + 1][c]] += 1  # bottom middle

            # print(f'[{r}][{c}] surrounded by: {adjacent}')
            if data[r][c] == 'L' and adjacent['#'] == 0:
                new_data[r][c] = '#'
                changed_seats = True
            elif data[r][c] == '#' and adjacent['#'] >= 4:
                new_data[r][c] = 'L'
                changed_seats = True
            # end seat
    return new_data


def part_1():
    data = []
    initialize(data)
    new_data = copy.deepcopy(seat_iteration(data))
    print('finished first iteration')
    iter = 1
    while not data == new_data:
        iter += 1
        data = copy.deepcopy(new_data)
        new_data = copy.deepcopy(seat_iteration(data))
        print(f'finished iteration {iter}')
    occupied = 0
    for row in new_data:
        for col in row:
            if col == '#':
                occupied += 1
    print(occupied)


def seat_iter_2(data):
    changed_seats = False
    new_data = copy.deepcopy(data)
    for r in range(len(data)):
        row = data[r]
        for c in range(len(row)):

            adjacent = {'L': 0, '#': 0, '.': 0}

            if not r == 0:
                if not c == 0:
                    nr = r - 1
                    nc = c - 1
                    adjacent_tile = data[nr][nc]  # top left
                    while not nr==0 and not nc==0 and adjacent_tile=='.':
                        nr -= 1
                        nc -= 1 # keep moving up and left
                        adjacent_tile = data[nr][nc]
                    adjacent[data[nr][nc]] += 1

                nr = r - 1  # top middle
                nc = c
                adjacent_tile = data[nr][nc]  # keep moving up rows
                while not nr == 0 and adjacent_tile == '.':
                    nr -= 1
                    adjacent_tile = data[nr][nc]
                adjacent[data[nr][nc]] += 1

                if not c == len(row) - 1:
                    nr = r - 1
                    nc = c + 1  # top right
                    adjacent_tile = data[nr][nc]  # keep moving up and right
                    while not nr == 0 and not nc == (len(row) - 1) and adjacent_tile == '.':
                        nr -= 1
                        nc += 1
                        adjacent_tile = data[nr][nc]
                    adjacent[data[nr][nc]] += 1

            if not c == 0:
                nr = r
                nc = c - 1  # middle left
                adjacent_tile = data[nr][nc]  # keep moving left
                while not nc == 0 and adjacent_tile == '.':
                    nc -= 1
                    adjacent_tile = data[nr][nc]
                adjacent[data[nr][nc]] += 1

                if not r == len(data) - 1:
                    nr = r + 1
                    nc = c - 1  # bottom left
                    adjacent_tile = data[nr][nc]  # keep moving down and left
                    while not nc == 0 and not nr == len(data) - 1 and adjacent_tile == '.':
                        nc -= 1
                        nr += 1
                        adjacent_tile = data[nr][nc]
                    adjacent[data[nr][nc]] += 1

            if not c == len(row) - 1:
                nr = r
                nc = c + 1  # middle right
                adjacent_tile = data[nr][nc]  # keep moving right
                while not nc == len(row) - 1 and adjacent_tile == '.':
                    nc += 1
                    adjacent_tile = data[nr][nc]
                adjacent[data[nr][nc]] += 1

                if not r == len(data) - 1:
                    nr = r + 1
                    nc = c + 1  # bottom right
                    adjacent_tile = data[nr][nc]  # keep moving down and right
                    while not nc == len(row) - 1 and not nr == len(data) - 1 and adjacent_tile == '.':
                        nc += 1
                        nr += 1
                        adjacent_tile = data[nr][nc]
                    adjacent[data[nr][nc]] += 1
            if not r == len(data) - 1:
                nr = r + 1
                nc = c   # bottom middle
                adjacent_tile = data[nr][nc]  # keep moving down
                while not nr == len(data) - 1 and adjacent_tile == '.':
                    nr += 1
                    adjacent_tile = data[nr][nc]
                adjacent[data[nr][nc]] += 1

            print(f'[{r}][{c}] surrounded by: {adjacent}')
            if data[r][c] == 'L' and adjacent['#'] == 0:
                new_data[r][c] = '#'
                changed_seats = True
            elif data[r][c] == '#' and adjacent['#'] >= 5:
                new_data[r][c] = 'L'
                changed_seats = True
            # end seat
    return new_data


def print_array(array: list):
    for row in array:
        for col in row:
            print(col, end='')
        print(' ')


def part_2():
    data = []
    initialize(data)
    print_array(data)
    new_data = copy.deepcopy(seat_iter_2(data))
    print('finished first iteration')
    iter = 1
    print_array(new_data)
    while not data == new_data:
        iter += 1
        data = copy.deepcopy(new_data)
        new_data = copy.deepcopy(seat_iter_2(data))
        print(f'finished iteration {iter}')
        print_array(new_data)
    occupied = 0
    for row in new_data:
        for col in row:
            if col == '#':
                occupied += 1
    print(occupied)



if __name__ == '__main__':
    part_2()
    # data = []
    # initialize(data)
    # print(data)
    # print(seat_iter_2(data))

