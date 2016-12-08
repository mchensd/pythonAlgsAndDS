def max_crossing_array(l, low, mid, high):
    temp_sum = 0
    left_sum = float("-inf")
    max_left = mid
    for e in range(mid, -1, -1):
        temp_sum += l[e]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = e

    temp_sum = 0
    right_sum = float("-inf")
    max_right = mid
    for e in range(mid+1, high+1):
        temp_sum += l[e]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = e

    return max_left, max_right, left_sum + right_sum

def max_subarray(l, low, high):
    if low == high:
        return low, high, l[low]

    else:
        mid = (low+high) // 2
        left_low, left_high, left_sum = max_subarray(l,low,mid)
        cross_low, cross_high, cross_sum = max_crossing_array(l, low, mid, high)
        right_low, right_high, right_sum = max_subarray(l, mid+1, high)

        if left_sum >= cross_sum and left_sum >= right_sum:
            return left_low, left_high, left_sum
        elif cross_sum >= right_sum and cross_sum >= left_sum:
            return cross_low, cross_high, cross_sum
        else:
            return right_low, right_high, right_sum
print(max_crossing_array([6,-5,10,-8,25,-35], 0, 3, 5))
print(max_crossing_array([-10,-5,-13,-26],0,2,3))

print(max_subarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7], 0, 15))

print(max_subarray([-5,-3,-6,-2,-6], 0, 4))

