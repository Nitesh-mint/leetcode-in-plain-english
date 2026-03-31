"""
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_table = set()
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hash_table:
                return [i, nums.index(dif)]
            hash_table.add(nums[i])
        return []

sln = Solution()
print(sln.twoSum([5,5], 10))
