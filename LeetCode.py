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


# 1929. Concatenation of Array
# Given an integer array nums of length n, you want to create an array ans of length 2n where
# ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

def getConcatenation(self, nums: list[int]) -> list[int]:
    return nums + nums


# 27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted,
# you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def removeElement(self, nums: list[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)


# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal
# substring
#  consisting of non-space characters only.
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

def lengthOfLastWord(self, s: str) -> int:
    words = s.split()
    if not words:
        return 0
    return len(words[-1])
