# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

def prod_array_except_self(nums):
    zero_count = 0
    zero_index = 0
    prod = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
            zero_index = i
        else:
            prod *= nums[i]
    if zero_count >= 2:
        return [0 for i in range(len(nums))]
    elif zero_count == 1:
        sol = [0 for i in range(len(nums))]
        sol[zero_index] = prod
        return sol
    else:
        return [int(prod/nums[i]) for i in range(len(nums))]
