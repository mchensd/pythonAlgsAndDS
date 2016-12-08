def second_max(ls):
    greatest = ls[0]
    second = float('-inf')
    for i in range(1, len(ls)):
        if ls[i] > greatest:
            second = greatest
            greatest = ls[i]
        elif ls[i] < greatest:
            if ls[i] > second:
                second = ls[i]
        
    return second

print(second([5,2,3]))
