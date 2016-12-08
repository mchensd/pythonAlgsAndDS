def check_mid(ls, num_inversions):
    mid_i = len(ls) // 2

    for i in range(len(ls[0: mid_i])):
        for j in range(len(ls[mid_i + 1:])):
            if ls[i] > ls[j+mid_i+1]:
                num_inversions += 1
    return num_inversions

def count_inversions(ls, num_inversions):
    if len(ls) == 2:  # base case
        return num_inversions + 1 if ls[0] > ls[1] else num_inversions

    else:
        mid = len(ls) // 2
        num_inversions = count_inversions(ls[0: mid+1], num_inversions)  # left check
        num_inversions = count_inversions(ls[mid:], num_inversions)  # right check
        num_inversions = check_mid(ls, num_inversions)

        return num_inversions

print(check_mid([7, 3, 6, 5, 2], 0))
print(check_mid([5,3,7,5,4,6,2], 0))

print(count_inversions([5,3,6,4,2], 0))  # 7

print(count_inversions([5,6,7,3,2,1], 0)) # 12

with open('integer_array.txt', 'r') as f:
    data = f.readlines()

    f.close()
for i in range(len(data)):
    data[i] = int(data[i].strip())
print(len(data))
print(count_inversions(data, 0))