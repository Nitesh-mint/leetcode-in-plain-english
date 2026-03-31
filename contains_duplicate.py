#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Input: nums = [1, 2, 3, 3]
# Output: true


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        duplicate_nums = set()
        if not nums:
            print("The list is empty")
            return False;
        for i in range(len(nums)):
            if nums[i] in duplicate_nums:
                return True 

            duplicate_nums.add(nums[i])
        return False

sln = Solution()
print(sln.hasDuplicate([1,2,2]))
