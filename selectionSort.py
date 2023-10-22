def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
# Example usage
if __name__ == "__main__":
    # Sample list to be sorted
    arr = [64, 25, 12, 22, 11]
    
    # Call the selection_sort function
    selection_sort(arr)
    
    # Output the sorted array
    print("Sorted array is:", arr)
