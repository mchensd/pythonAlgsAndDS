# Problem: N white and black balls are arranged in a row. Determine the least number of swaps necessary 
# to shift all the white balls to the left of all the black balls, while only being allowed to swap two
# neighbouring balls at a time.

### Algorithm Design:
# Take a group of unsorted black or white marbles, for this example we will use 'wbbwbbww'
# In order to sort all the whites on the left and blacks on the right, we will first sort the first half so that
# it will be 'wwbb' and the second half so that it will also be 'wwbb'
# We will use recursion to do so
# Once we have sorted both halves, we swap the b's and the w's in the middle
# 'wwbbwwbb' turns into 'wwwwbbbb' and we are done.
import copy
def sort_marbles(pattern, swaps):
    if len(pattern) == 1:
        return pattern, swaps

    else:
        mid = len(pattern) // 2
        left_pattern, swaps = sort_marbles(pattern[0: mid], swaps)
        right_pattern, swaps = sort_marbles(pattern[mid:], swaps)
        pattern = left_pattern + right_pattern
        # Checks for cases where we need to swap consecutive w's and b's in the middle
        if pattern[mid] == 'w' and pattern[mid-1] == 'b':  # need this line to filter out cases like 'bbb'
            swapped_pat = copy.copy(pattern)
            b_count = 0
            w_count = 0
            for i in range(len(pattern[0: mid])):
                if pattern[i] == 'b':  # b's need to be placed in the later half
                    b_count += 1
                    swapped_pat.remove('b')
                    swapped_pat.append('b')
            for i in range(mid, len(pattern)):
                if pattern[i] == 'w':  # w's should already be in the beginning half
                    w_count += 1
            # Number of swaps required will be the consecutive w's in the middle * consecutive b's in the middle
            swaps += w_count * b_count
            return swapped_pat, swaps
        return pattern, swaps

print(sort_marbles(['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], 0))  # 6 - correct
print(sort_marbles(['b', 'b', 'b', 'w', 'w', 'w'], 0)) #9 - correct
print(sort_marbles(['w', 'b', 'b', 'b'], 0))  # 0- correct
print(sort_marbles(['b', 'w', 'b', 'b', 'w', 'w', 'b', 'w', 'w'], 0))  #15 - correct
print(sort_marbles(['b', 'w', 'w', 'b', 'b', 'w'], 0))  # 5 - correct