def binary_search():
    """
    Perform binary search on a sorted array to find the index of the target element.
    Returns -1 if the target is not found in the array.
    """
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = int(input("Enter the target: "))
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(binary_search())
