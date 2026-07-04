'''

Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Input: nums = [1,2,3,4,5]
Output: true

Input: nums = [5,4,3,2,1]
Output: false

'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1=num2=num3=max(nums)+1
        for i in nums:
            if i<num1:
                num1=i 
                continue 
            if num1<i<num2:
                num2=i 
                continue 
            if num2<i<num3:
                num3=i
                return True
        return False
