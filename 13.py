from numpy import lcm


data = []
with open('day13_input.txt', 'r') as infile:
    for line in infile:
        data.append(line)

def part_1():
    target_departure_time = int(data[0])
    buses = [int(b) for b in data[1].split(',') if b != 'x']

    bus_departs = {}
    for b in buses:
        depart_time = 0
        while depart_time < target_departure_time:
            depart_time += b
        bus_departs[depart_time] = b

    times = []
    for time, id in bus_departs.items():
        times.append(time)
    times.sort()
    print(f'earliest bus is {bus_departs[times[0]]}, answer is {bus_departs[times[0]] * (times[0] - target_departure_time)}')


# my original solution for part 2 which takes too long to compute the final answer.
def part_2_old():
    buses = [b for b in data[1].split(',')]

    min_time = 100000000000000  # to start at beginning, use buses[0]
    min_time -= min_time % int(buses[0])

    checking_time = min_time
    break_loop = False
    while not break_loop:
        valid_time = True
        for i, bus in enumerate(buses):
            print(f'{i}, {bus}')
            if bus != 'x':
                bus = int(bus)
                print(f'checking {checking_time} + {i} % {bus} == 0')
                if not (checking_time + i) % bus == 0:
                    valid_time = False
        if valid_time:
            break_loop = True
            print(f'broke loop at time {checking_time}')
            break
        checking_time += int(buses[0])


# credit to https://github.com/whiplashoo/advent_of_code_2020/blob/main/day13.py
# for helping me understand a more time optimized solution.
def part_2():
    buses = [b for b in data[1].split(',')]
    time = 0
    matched_buses = [int(buses[0])]

    break_loop = False
    while not break_loop:
        blcm = int(buses[0])
        for bus in matched_buses:
            if bus != 'x':
                blcm = lcm(blcm, int(bus))
        time += blcm

        for i, bus in enumerate(buses):
            if bus != 'x':
                bus = int(bus)
                if (time + i) % bus == 0 and bus not in matched_buses:
                    matched_buses.append(bus)

        if len(matched_buses) == len(buses) - buses.count('x'):
            break_loop = True

    print(time)

part_2()