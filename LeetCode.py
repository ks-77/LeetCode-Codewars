# 1. Two Sum
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def twoSum(nums: list[int], target: int) -> list[int]:
    res = {}
    for i in range(len(nums)):
        if target - nums[i] in res:
            return [res[target - nums[i]], i]
        res[nums[i]] = i


# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2


def searchInsert(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)
