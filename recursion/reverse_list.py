def reverse_list(l):
    if len(l) == 1:
        return l
    else:
        reversed = reverse_list(l[1:]) + [l[0]]
        return reversed

print(reverse_list([1,2,3]))
print(reverse_list(list(range(10))))

