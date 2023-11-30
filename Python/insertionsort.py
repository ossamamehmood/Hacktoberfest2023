def insertionSort(arr):
    n = len(arr)
      
    if n <= 1:
        return
 
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Take user input for the array elements
input_str = input("Enter elements of the array separated by spaces: ")
arr = [int(x) for x in input_str.split()]

insertionSort(arr)
print("Sorted array:", arr)


//insertion sort in python
