"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example:

    Input: s = "Was it a car or a cat I saw?"
    Output: true

    Input: s = "tab a cat"
    Output: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s.lower() if c.isalnum())
        pointer_a = 0  # point to the first
        poitner_b = len(cleaned) - 1  # point to the last

        while pointer_a < poitner_b:
            if cleaned[pointer_a] != cleaned[poitner_b]:
                return False

            pointer_a = pointer_a + 1
            poitner_b = poitner_b - 1

        return True


sln = Solution()
print(sln.isPalindrome("Was it a car or a cat I saw?"))
print(sln.isPalindrome("tab a cat"))
print(sln.isPalindrome("No lemon, no melon"))
print(sln.isPalindrome("!!??!!"))
