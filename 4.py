import re
import traceback

data = []

with open('day4_input.txt', mode='r') as infile:
    for line in infile:
        data += [line]

line = 0
valid = 0
try:
    while line < len(data):  #continue through all the data
        print(f'starting at line {line}')
        required_fields = {'byr': None, 'iyr': None, 'eyr': None, 'hgt': None, 'hcl': None, 'ecl': None, 'pid': None}
        while line < len(data) and len(data[line]) > 2:  # continue through current passport
            fields_and_vals = data[line].split(' ')  # split line on space
            for x in fields_and_vals:
                f_a_v = x.split(':')
                field = f_a_v[0].replace("\n", "")
                value = f_a_v[1].replace("\n", "")
                required_fields[field] = value
            line += 1
        # finished with passport
        print(f'finished at line {line}')
        line += 1
        print(f'required fields are {required_fields}')
        invalid = False
        for key, val in required_fields.items():
            print(f'testing {required_fields[key]}')
            if required_fields[key] is None:
                print('not valid')
                invalid = True
                break
            if key == 'byr':
                val = int(val)
                if not isinstance(val, int) or not 1920 <= val <= 2002:
                    invalid = True
                    break
            if key == 'iyr':
                val = int(val)
                if not isinstance(val, int) or not 2010 <= val <= 2020:
                    invalid = True
                    break
            if key == 'eyr':
                val = int(val)
                if not isinstance(val, int) or not 2020 <= val <= 2030:
                    invalid = True
                    break
            if key == 'hgt':
                if re.search('^.*cm.*$', val):
                    print(f'{val} contains cm')
                    h_val = int(val[0:-2])
                    if not 150 <= h_val <= 193:
                        invalid = True
                        break
                    else:
                        print(f'{val} is a valid height')
                    # cm
                    pass
                elif re.search('^.*in.*$', val):
                    print(f'{val} contains in')
                    h_val = int(val[0:-2])
                    if not 59 <= h_val <= 76:
                        invalid = True
                        break
                    else:
                        print(f'{val} is a valid height')
                    pass
                else:  # does not contain cm or in
                    invalid = True
                    break
            if key == 'hcl':
                if not re.fullmatch('[#]{1}[a-f0-9]{6}', val):
                    print(f'{val} is not valid hcl')
                    invalid = True
                    break
                else:
                    print(f'{val} is a valid hcl')
            if key == 'ecl':
                valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if val not in valid_eye_colors:
                    invalid = True
                    break
            if key == 'pid':
                if not re.fullmatch('[0-9]{9}', val):
                    invalid = True
                    break
        if not invalid:
            print('valid')
            valid += 1

except IndexError as e:
    traceback.print_exc()
    print(f'tried to access data[{line}]')

print(f'valid: {valid}')
