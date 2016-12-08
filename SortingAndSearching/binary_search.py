def search_binary(ls, target):  # takes a sorted list ls and returns true if target is in it else false
    mid = len(ls) // 2
    first = 0
    last = len(ls) - 1

    found = False

    while not found and first <= last:
        os = ls[mid]

        if os == target:
            found = True
        else:
            if target > os:
                first = mid + 1
            elif target < os:
                last = mid -  1
            mid = (first + last + 1) // 2
    return found

def search_binary_rec(ls, target):
    first = 0
    last = len(ls) - 1
    mid = len(ls) // 2
    found = False

    while not found and first <= last:
        os = ls[mid]
        mid = (first+last+1) // 2
        if os == target:
            found = True
        else:
            if target > os:
                return search_binary_rec(ls[mid+1 :], target)
            elif target < os:
                return search_binary_rec(ls[:mid], target)

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(search_binary(testlist, 3))
print(search_binary(testlist, 13))
print(search_binary_rec(testlist, 3))
print(search_binary_rec(testlist, 13))