q = int(input())

for z in range(q):
    a = list(input())
    b = list(input())

    j = 0  # b index

    can_convert = False
    for i in range(len(a)):
        if a[i].lower() == b[j].lower():
            j += 1
            a[i] = a[i].upper()
            if j == len(b):
                can_convert = True
                break

        else:
            if a[i].isupper():
                can_convert = False
                break

    if not can_convert:
        print('NO')
    else:
        compare_b = ''.join(b)
        compare_str = ''
        for i in a:
            if i.isupper():
                compare_str += i
        if compare_str == compare_b:
            print('YES')
        else:
            print('NO')
