q = int(input())
for z in range(q):
    a = list(input())
    b = list(input())
    
    j = 0  # b index
    
    can_convert = False
    for i in range(len(a)):
        if a[i].lower() == b[j].lower():
            a[i] = a[i].upper()
            j += 1
            if j == len(b):
                can_convert = True
                break
        else: 
            if a[i].isupper():  # if we can't delete it:
                can_convert=False
                break
    if not can_convert:
        print('NO') 
    else:  # check for capitals after our found string
        compare_str = ""
        for i in range(len(a)):
            if a[i].isupper():
                compare_str += a[i]
        if compare_str == ''.join(b):
            print('YES')
        else:
            print('NO')