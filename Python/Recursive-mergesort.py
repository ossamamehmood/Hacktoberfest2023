def merge_sort(arr):
    # Base case: If our array is small enough to work with, it's already sorted.
    if len(arr) <= 1:
        return arr

    # Let's divide our array into two parts.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Now, we'll sort both halves separately by calling merge_sort on them.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Finally, we'll merge the two sorted halves back together and return the result.
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Here, we compare elements from both halves and put them in order.
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # After we've compared and added as many elements as we can, we might have some leftovers.
    # Let's make sure to add any remaining elements from both halves (if there are any).
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    # Our merged and sorted result is ready to go.
    return result

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Here's the sorted array:", sorted_arr)
