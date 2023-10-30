def longest_increasing_subsequence(nums):
    if not nums:
        return []

    n = len(nums)
    # Initialize an array to store the length of the longest increasing subsequence ending at each position
    lis_lengths = [1] * n

    # Initialize a list to store the actual subsequences
    subsequences = [[] for _ in range(n)]
    subsequences[0].append(nums[0])

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                if lis_lengths[i] < lis_lengths[j] + 1:
                    lis_lengths[i] = lis_lengths[j] + 1
                    subsequences[i] = subsequences[j][:]  # Clone the previous subsequence
        subsequences[i].append(nums[i])

    # Find the position of the longest increasing subsequence
    max_length_index = lis_lengths.index(max(lis_lengths))

    return subsequences[max_length_index]

sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest_increasing_subsequence(sequence)
print(result)  # Should print [10, 22, 33, 50, 60, 80]
