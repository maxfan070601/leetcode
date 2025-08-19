# 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
#
#
#
# Example 1:
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:
#
# Input: nums = [5], k = 1
# Output: 5.00000
#
#
# Constraints:
#
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

def max_avg_subarray(nums: list[int], k: int) -> float:
    max_avg = -float('inf')
    if k == 1:
        return max(nums)
    else:
        for i in range(len(nums)-k+1):
            avg = 0
            for j in range(i, i+k):
                avg += nums[j]
            avg /= k
            if avg > max_avg:
                max_avg = avg
        return max_avg


def max_avg_subarray_faster(nums: list[int], k: int) -> float:
    max_avg = -float('inf')
    if k == 1:
        return max(nums)
    else:
        avg = sum([nums[i] for i in range(0, len(nums)-k+1)])/k
        max_avg = max(avg, max_avg)
        count = 0
        while count < len(nums) - k: # figure out why this is the bounds & test case 1 overshooting
            avg -= nums[count]/k
            avg += nums[k+count]/k
            count += 1
            max_avg = max(avg, max_avg)
    return max_avg




print(max_avg_subarray_faster([5, 3, 7], 2))