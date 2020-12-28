values = []

with open('day1_input.txt', mode='r') as infile:
    for num in infile:
        values.append(int(num.rstrip()))

target_sum = 2020
for n in values:
    for m in values:
        for p in values:
            if n + m + p == target_sum:
                print(f'{n} and {m} and {p} add to {target_sum} and multiply to {m * n * p}.')


print('done')
