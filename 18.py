def prep(exp: str):
    items = list(exp.replace(' ', ''))
    for i, val in enumerate(items):
        non_ints = ['+', '*', '(', ')']
        if val not in non_ints:
            items[i] = int(val)
    return items


def evaluate(exp: list):
    total = 0
    current_item = exp[0]
    current_operator = '+'
    i = 0

    while True:
        if current_item == '(':  # read until paren stack clear, evaluate expression, assign to current_item, update i
            paren_stack = ['(']
            inner_exp = []
            while not (current_item == ')' and not paren_stack):
                i += 1
                current_item = exp[i]
                if current_item == '(':
                    paren_stack.append(current_item)
                    inner_exp.append(current_item)
                elif current_item == ')':
                    paren_stack.pop()
                    if paren_stack:
                        inner_exp.append(current_item)
                else:
                    inner_exp.append(current_item)

            current_item = evaluate(inner_exp)

        if isinstance(current_item, int):
            if current_operator == '+':
                total += current_item
            elif current_operator == '*':
                total *= current_item

        # if end of exp then break, else get next operator, next item, and continue loop until end of expression
        if i < len(exp) - 2:
            i += 1
            current_operator = exp[i]
            i += 1
            current_item = exp[i]
        else:
            break
    return total


def advanced_evaluate(exp: list):
    total = 0
    current_item = exp[0]
    current_operator = '+'
    i = 0

    multiplicands = []

    while True:
        if current_item == '(':  # read until paren stack clear, evaluate expression, assign to current_item, update i
            paren_stack = ['(']
            inner_exp = []
            while not (current_item == ')' and not paren_stack):
                i += 1
                current_item = exp[i]
                if current_item == '(':
                    paren_stack.append(current_item)
                    inner_exp.append(current_item)
                elif current_item == ')':
                    paren_stack.pop()
                    if paren_stack:
                        inner_exp.append(current_item)
                else:
                    inner_exp.append(current_item)

            current_item = advanced_evaluate(inner_exp)

        if isinstance(current_item, int):
            if current_operator == '+':
                total += current_item
            elif current_operator == '*':
                multiplicands.append(total)
                total = current_item

        # if end of exp then break, else get next operator, next item, and continue loop until end of expression
        if i < len(exp) - 2:
            i += 1
            current_operator = exp[i]
            i += 1
            current_item = exp[i]
        else:
            break
    if multiplicands:
        for m in multiplicands:
            total *= m
    return total


data = []
with open('day18_input.txt', 'r') as infile:
    for line in infile:
        data.append(line.strip())

file_sum = 0
for expression in data:
    exp_result = advanced_evaluate(prep(expression))
    print(exp_result)
    file_sum += exp_result

print(file_sum)
