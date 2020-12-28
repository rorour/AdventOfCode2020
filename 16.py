data = []
with open('day16_input.txt', 'r') as infile:
    for line in infile:
        data.append(line.strip('\n'))

fields = {}  # {field name: [acceptable values]}

i = 0
line = data[i]
while not line == '':
    field = line.split(':')
    field_name = field[0]
    field_ranges = field[1].strip().split('or')

    min1 = int(field_ranges[0].split('-')[0])
    max1 = int(field_ranges[0].split('-')[1])
    min2 = int(field_ranges[1].split('-')[0])
    max2 = int(field_ranges[1].split('-')[1])

    fields[field_name] = []
    for a in range(min1, max1 + 1):
        fields[field_name].append(a)
    for b in range(min2, max2 + 1):
        fields[field_name].append(b)

    i += 1
    line = data[i]

valid_tickets = []

i += 2
your_ticket = data[i]
valid_tickets.append(your_ticket)

while not line == 'nearby tickets:':
    i += 1
    line = data[i]

invalid_ticket_vals = []

for line in data[i + 1:]:
    ticket_vals = [int(z) for z in line.split(',')]
    valid_ticket = True
    for val in ticket_vals:
        found_acceptable_field = False
        for acceptable_val_list in fields.values():
            if val in acceptable_val_list:
                found_acceptable_field = True
                break
        if not found_acceptable_field:
            invalid_ticket_vals.append(val)
            valid_ticket = False
    if valid_ticket:
        valid_tickets.append(line)

print(sum(invalid_ticket_vals))

valid_tickets = [t.split(',') for t in valid_tickets]

# maintain list of potential field names for each position on ticket. start with all & remove invalid.
possible_fields = {}  # {position number: [possible field names]}
for f in range(0, len(fields)):
    possible_fields[f] = [k for k in fields.keys()]

for ticket in valid_tickets:
    ticket = [int(t) for t in ticket]
    for pos, val in enumerate(ticket):
        for field_name, valid_values in fields.items():
            if field_name in possible_fields[pos] and val not in valid_values:
                possible_fields[pos].remove(field_name)

all_fields_identified = False
while not all_fields_identified:

    for pos, field_names in possible_fields.items():
        if len(field_names) == 1:
            for p, f_n in possible_fields.items():
                if not p == pos and field_names[0] in f_n:
                    f_n.remove(field_names[0])

    all_fields_identified = True
    for pos, field_names in possible_fields.items():
        if not len(field_names) == 1:
            all_fields_identified = False

departure_product = 1
your_ticket_values = [int(v) for v in your_ticket.split(',')]
for pos, field_names in possible_fields.items():
    if field_names[0].startswith('departure'):
        departure_product *= your_ticket_values[pos]

print(departure_product)


