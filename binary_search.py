"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn)O(logn) time.

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low} + high: {high} and mid: {mid}")
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1


sln = Solution()
print(sln.search([-1, 0, 2, 4, 6, 8], 4))
