def merge(ls, p, q, m):
    if len(ls) == 1:
        return ls, p, q, m

    ls_left, p1, q1, m1 = merge(ls[p:m], 0, m-1, len(ls[p:m]) // 2)
    ls_right, p2, q2, m2 = merge(ls[m:], 0, len(ls[m:]) - 1, len(ls[m:])//2)

    i = 0
    k = 0

    #ls_left.append(float('inf'))
    #ls_right.append(float('inf'))
    sorted = []
    for e in range(q - p + 1):
        if ls_left[i] >= ls_right[k]:
            sorted.append(ls_right[k])
            k += 1
            if k == len(ls_right):  # end of the right half list
                sorted.extend(ls_left[i:])
                break
        elif ls_right[k] > ls_left[i]:
            sorted.append(ls_left[i])
            i += 1

            if i == len((ls_left)):  # end of left half list
                sorted.extend(ls_right[k:])
                break

    return sorted, p, q, m

#print(merge([8,6,1,5], 0, 3, 2))
print(merge([6,1,6,3,6,3,2,1], 0, 7, 4))



