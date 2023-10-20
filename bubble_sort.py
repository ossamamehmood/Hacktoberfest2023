def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize and break early if the list is already sorted
        swapped = False
        
        # Last i elements are already in place, so we don't need to compare them again
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array:", my_list)
