data = []

with open('day8_input.txt', 'r') as infile:
    for line in infile:
        data.append(line)


def part_1():
    current_line = 0
    acc = 0
    run_lines = []

    while current_line < len(data):
        if current_line in run_lines:
            print(f'acc is {acc}')
            break
        run_lines.append(current_line)
        print(f'at line {current_line}')
        cmd = data[current_line]
        if 'acc' in cmd:
            val = int(cmd[4:-1])
            acc += val
            current_line += 1
        elif 'jmp' in cmd:
            val = int(cmd[4:-1])
            current_line += val
        elif 'nop' in cmd:
            current_line += 1


def part_2():
    for current_instruction in range(len(data)):
        changed = True
        old_line_val = data[current_instruction]
        if 'jmp' in old_line_val:
            new_line_val = 'nop' + old_line_val[3:]
            data[current_instruction] = new_line_val
        elif 'nop' in old_line_val:
            new_line_val = 'jmp' + old_line_val[3:]
            data[current_instruction] = new_line_val
        else:
            changed = False

        if changed:
            current_line = 0
            acc = 0
            run_lines = []

            while current_line < len(data):
                if current_line in run_lines:
                    print(f'ran into repeated line.')
                    data[current_instruction] = old_line_val
                    break
                run_lines.append(current_line)
                cmd = data[current_line]
                if 'acc' in cmd:
                    val = int(cmd[4:].replace('\n', ''))
                    acc += val
                    current_line += 1
                elif 'jmp' in cmd:
                    val = int(cmd[4:].replace('\n', ''))
                    current_line += val
                elif 'nop' in cmd:
                    current_line += 1
            if current_line >= len(data):
                print('reached end of file.')
                print(f'acc is {acc}**********************************************************')


part_2()
