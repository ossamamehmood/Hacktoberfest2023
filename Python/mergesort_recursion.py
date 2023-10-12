def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr

    stack = [[i] for i in arr]

    while len(stack) > 1:
        new_stack = []
        for i in range(0, len(stack) - 1, 2):
            merged = merge(stack[i], stack[i + 1])
            new_stack.append(merged)
        if len(stack) % 2 == 1:
            new_stack.append(stack[-1])
        stack = new_stack

    return stack[0]

# Take user input for the array
input_str = input("Enter space-separated elements: ")
user_input = input_str.split()
arr = [int(x) for x in user_input]

# Call the merge_sort function
sorted_arr = merge_sort(arr)

# Display the sorted array
print("Sorted array is:", sorted_arr)
#In this implementation, the merge function is used for merging two subarrays efficiently.
#  The main optimization is in the iterative merging process using a stack, which eliminates the need for recursive function calls. 
# This can be more efficient in practice, especially for large arrays.
#The previous solution consists some loopholes such that due to unnecessary recursive calls 
# there is some extra use of memory which is avoided in this solution 