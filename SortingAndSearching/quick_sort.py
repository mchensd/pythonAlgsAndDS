def quick_sort(ls):
    if  len(ls) == 1:
        return ls

    else:
        pivot = ls[0]
        left_index = 1
        right_index = len(ls) - 1

        while left_index <= right_index:
            if ls[left_index] < pivot:  # in the right position
                left_index += 1

            if ls[right_index] >= pivot:  # in the right position
                right_index -= 1

            if left_index < right_index:
                if ls[left_index] >= pivot and ls[right_index] < pivot:
                # swap
                    left_item = ls[left_index]
                    ls[left_index] = ls[right_index]
                    ls[right_index] = left_item


        ls[0] = ls[right_index]
        ls[right_index] = pivot

        left = quick_sort(ls[0:right_index])
        right = quick_sort(ls[right_index:])

        sorted = left + list(pivot) + right
        return sorted


print(quick_sort([7,2,3,9,6,5,8]))
print(quick_sort([9,8]))



