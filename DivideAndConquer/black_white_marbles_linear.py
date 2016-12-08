# Problem: N white and black balls are arranged in a row. Determine the least number of swaps necessary
# to shift all the white balls to the left of all the black balls, while only being allowed to swap two
# neighbouring balls at a time.

def sort_marbles(pattern):
    w_count = 0
    b_count = 0

    for char in pattern:
        if char == "b":
            b_count += 1
        else:
            w_count += 1

    swaps = 0
    for e in range(len(pattern)):
        if pattern[e] == 'w':
            w_count -= 1
        else:
            if w_count > 0:  # b before a w, swapping needs to be done
                current = pattern[e]
                if pattern[e+1] == 'w':
                    pattern[e] = 'w'
                    pattern[e+1] = current
                    w_count -= 1
                    swaps += 1
                elif pattern[e+1] == 'b':  # consecutive b's
                    len_bs = 2
                    for i in range(e+2, len(pattern)):  # finding the length of consecutive b's
                        if pattern[i] == 'b':
                            len_bs += 1
                        else:  # perform the swap now
                            break
                    # swap the consecutive b's with the w
                    pattern[e+1: e + len_bs + 1] = 'b' * len_bs
                    pattern[e] = 'w'

                    swaps += len_bs
                    w_count -= 1
            else:
                break
    return swaps

print(sort_marbles(['w','b','b','w']))  # 2 - correct
print(sort_marbles(['w', 'b', 'w', 'b', 'b', 'b', 'w'])) # 5 - correct
print(sort_marbles(['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b']))  # 6 - correct
print(sort_marbles(['b', 'b', 'b', 'w', 'w', 'w'])) #9 - correct
print(sort_marbles(['w', 'b', 'b', 'b']))  # 0- correct
print(sort_marbles(['b', 'w', 'b', 'b', 'w', 'w', 'b', 'w', 'w']))  #15 - correct
print(sort_marbles(['b', 'w', 'w', 'b', 'b', 'w']))  # 5 - correct



