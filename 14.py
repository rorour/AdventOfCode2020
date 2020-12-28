data = []
version = 2 # part 1 or 2 of the problem statement
with open('day14_input.txt', 'r') as infile:
    for line in infile:
        data.append(line.strip())

mask = []
memory = {}
for line in data:
    line = [l.strip() for l in line.split('=')]
    if version == 1:
        if line[0] == 'mask':
            mask = []
            for bit, val in enumerate(line[1]):
                if val != 'X':
                    mask.append((bit, val))
        else:
            mem_loc = line[0].strip('mem[').strip(']')
            decimal_val = int(line[1])
            # convert decimal val to binary, make string and pad with 0's, then apply mask, revert to decimal and store
            binary_val = list(str(bin(decimal_val)[2:]).rjust(36, '0'))
            for tup in mask:
                binary_val[(int(tup[0]))] = tup[1]
            binary_val = ''.join(binary_val)
            decimal_val = int(str(binary_val), 2)
            memory[mem_loc] = decimal_val
            print(mem_loc, decimal_val, binary_val)
    elif version == 2:
        if line[0] == 'mask':
            mask = line[1]
        else:
            mem_loc = line[0].strip('mem[').strip(']')
            val_to_store = line[1]
            dec_mem_addr = int(mem_loc)
            bin_addr = list(str(bin(dec_mem_addr)[2:]).rjust(36, '0'))
            floating_indexes = []
            for i, bit in enumerate(mask):
                if bit == '1':
                    bin_addr[int(i)] = bit
                elif bit == 'X':
                    floating_indexes.append(i)
            # get list of all possible mem addrs
            mem_addrs = []
            num_poss_addrs = 2 ** len(floating_indexes)
            for n in range(0, num_poss_addrs):  # n in binary represents vals of each index in order
                new_bin_addr = bin_addr
                bin_n = bin(n)[2:].rjust(len(floating_indexes), '0')
                a = 0
                for fi in floating_indexes:
                    new_bin_addr[fi] = bin_n[a]
                    a += 1
                mem_addrs.append(''.join(new_bin_addr))

            print(mem_addrs)
            print(num_poss_addrs)

            for b_addr in mem_addrs:
                decimal_addr = int(str(b_addr), 2)
                memory[decimal_addr] = int(val_to_store)

mem_sum = 0
for loc, val in memory.items():
    mem_sum += val

print(mem_sum)
