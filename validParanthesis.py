"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example:

    Input: s = "[]"
    Output: true

    Input: s = "([{}])"
    Output: true

    Input: s = "[(])"
    Output: false

Explanation: The brackets are not closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0 or s == "":
            return False

        stack = []
        bracketHashMap = {"}": "{", "]": "[", ")": "("}

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if stack == []:
                    return False
                if stack.pop() != bracketHashMap.get(char):
                    return False

        return stack == []


sln = Solution()
print(sln.isValid("[]"))
print(sln.isValid("([{}])"))
print(sln.isValid("[(]"))
print(sln.isValid("[[["))
print(sln.isValid("]]]"))
