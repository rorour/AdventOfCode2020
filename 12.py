data = []

with open('day12_input.txt', 'r') as infile:
    for line in infile:
        data.append(line)


def part_1():
    facing = 'E'
    ns_val = 0  # positive val is north, negative south
    ew_val = 0  # positive val east, negative west

    for line in data:
        direction = line[0]
        magnitude = int(line[1:])
        rotating = False

        R = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        L = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}

        if direction == 'R':
            rotating = True
            while magnitude > 0:
                facing = R.get(facing)
                magnitude -= 90
        elif direction == 'L':
            rotating = True
            while magnitude > 0:
                facing = L.get(facing)
                magnitude -= 90
        elif direction == 'F':
            direction = facing

        if not rotating:
            if direction == 'N':
                ns_val += magnitude
            elif direction == 'S':
                ns_val -= magnitude
            elif direction == 'E':
                ew_val += magnitude
            elif direction == 'W':
                ew_val -= magnitude

    print(f'final coordinates NS{ns_val}, EW{ew_val}')
    print(abs(ew_val) + abs(ns_val))


def part_2():
    # ship starts at origin and waypoint starts at 10E, 1N
    ship_ns_val = 0  # positive val is north, negative south
    ship_ew_val = 0  # positive val east, negative west
    wp_ns_val = 1
    wp_ew_val = 10

    for line in data:
        direction = line[0]
        magnitude = int(line[1:])

        if direction == 'N':
            wp_ns_val += magnitude
        elif direction == 'S':
            wp_ns_val -= magnitude
        elif direction == 'E':
            wp_ew_val += magnitude
        elif direction == 'W':
            wp_ew_val -= magnitude
        elif direction == 'F':
            ship_ns_val += magnitude * wp_ns_val
            ship_ew_val += magnitude * wp_ew_val
        elif direction == 'L':
            times_to_rotate = int(magnitude / 90)
            for i in range(0, times_to_rotate):
                old_ns = wp_ns_val
                old_ew = wp_ew_val
                wp_ns_val = old_ew
                wp_ew_val = -1 * old_ns
        elif direction == 'R':
            times_to_rotate = int(magnitude / 90)
            for i in range(0, times_to_rotate):
                old_ns = wp_ns_val
                old_ew = wp_ew_val
                wp_ns_val = -1 * old_ew
                wp_ew_val = old_ns
    print(abs(ship_ns_val)+ abs((ship_ew_val)))
    

part_2()
