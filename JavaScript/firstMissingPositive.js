/**
 * This is solution for problem First Missing Positive on Leetcode
 * Link for this problem: https://leetcode.com/problems/first-missing-positive/
 */

/**
 * @param {number[]} nums
 * @return {number}
 */

const firstMissingPositive = function (nums) {
    // let length = nums.length;
    if (nums.length == 0) return 1;
    if (nums.length == 1) {
        if (nums[0] == 1) return 2;
        else return 1;
    }
    let nums2 = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] <= 0) continue;
        nums2[nums[i]] = nums[i];
    }
    // let length2 = nums2.length;
    if (nums2.length == 0) return 1;
    for (let i = 1; i < nums2.length; i++) {
        if (!nums2[i]) return i;
    }
    return nums2[nums2.length - 1] + 1;
};
