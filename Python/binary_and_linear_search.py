def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Input the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Input the number to find
target = int(input("Enter the number you want to find: "))

# Choose the search method
print("Select a search method:")
print("1. Linear Search")
print("2. Binary Search")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    index = linear_search(numbers, target)
elif choice == 2:
    numbers.sort()  # Binary search requires a sorted list
    index = binary_search(numbers, target)
else:
    print("Invalid choice. Please select 1 or 2.")
    index = -1

if index != -1:
    print(f"{target} found at index {index}.")
else:
    print(f"{target} not found in the list.")
