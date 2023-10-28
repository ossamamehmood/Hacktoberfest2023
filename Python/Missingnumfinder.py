def find_missing_number(nums, n):
    # Calculate the expected sum of numbers from 1 to N
    expected_sum = (n * (n + 1)) // 2

    # Calculate the actual sum of numbers in the array
    actual_sum = sum(nums)

    # The difference is the missing number
    missing_number = expected_sum - actual_sum

    return missing_number

# Example usage:
arr = [1, 2, 4, 6, 3, 7, 8]
N = max(arr)  # Assuming N is the maximum number in the array
result = find_missing_number(arr, N)
print("Missing number:", result)
