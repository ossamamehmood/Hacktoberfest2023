
"""
Description:
Given an array nums and a target value k, 
find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Input:  nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation:
because the subarray [1, -1, 5, -2] sums to 3 and is the longest.

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation:
because the subarray [-1, 2] sums to 1 and is the longest.

"""


"""
Algorithm
Need to use hash table and cumulative sum, then the benefit of establishing cumulative sum is obvious, if the current cumulative sum is exactly equal to k, then the sub-array from the beginning to this position is a satisfactory solution, but not necessarily the longest Sub-array, and use a hash table to establish the mapping between the cumulative sum and its coordinates, we analyze from the example given in the title:

nums: [1, -1, 5, -2, 3], k = 3

sums: [1, 0, 5, 3, 6]

"""

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mp = {0: -1}
        s = ans = 0
        for i, v in enumerate(nums):
            s += v
            if s - k in mp:
                ans = max(ans, i - mp[s - k])
            if s not in mp:
                mp[s] = i
        return ans