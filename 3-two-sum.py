'''
https://leetcode.com/problems/two-sum/
3. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''    

def two_sum(nums, target):
  for index in range(len(nums)):
    difference = target - nums[index]
    comparison_array = nums[index+1:]
    if difference in comparison_array:
      return print("[{}, {}]".format(index, comparison_array.index(difference) + index + 1))

two_sum([2,7,11,15], 9)
two_sum([3,2,4], 6)
two_sum([3,3], 6)



