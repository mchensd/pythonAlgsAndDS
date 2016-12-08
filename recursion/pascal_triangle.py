

def generate_pascal(rows):
    pascal_rows = [None for i in range(rows)]
    for i in range(len(pascal_rows)):
        pascal_rows[i] = [1] * (i+1)

    if len(pascal_rows) >= 3:  # need to do some calculations
        for i in range(2, len(pascal_rows)):
            for e in range(1, len(pascal_rows[i])-1):
                pascal_rows[i][e] = pascal_rows[i-1][e-1] + pascal_rows[i-1][e]
    for i in range(len(pascal_rows)):
        for e in range(len(pascal_rows[i])):
            pascal_rows[i][e] = str(pascal_rows[i][e])

    indent_size =  rows-1
    pretty_pascal = ''  # the representation of the list
    for i in range(len(pascal_rows)):
        pretty_pascal += ' '*(indent_size - i)
        pretty_pascal += ' '.join(pascal_rows[i])
        pretty_pascal += '\n'
    return pretty_pascal

generate_pascal(2)
generate_pascal(3)
generate_pascal(6)

print(generate_pascal(10))
