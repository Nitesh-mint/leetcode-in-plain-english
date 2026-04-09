"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Input: head = [0,1,2,3]

Output: [3,2,1,0]

Input: head = []

Output: []

GEMINI CHAT: https://gemini.google.com/share/8f8215d3a507
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# list ko last samma jane store the previous
"""

We use three poitners:
prev = store_the_previous
currnet = store_the_current
next = store_the_next

[1] -> [2] -> [3] -> None
[1] -> None : others is at the  next -> [2] which points
to the other nodes
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


sln = Solution()
listHead = ListNode(1, None)
current = listHead
for i in range(2, 6):
    next = ListNode(i, None)
    current.next = next
    current = next

reversedHead = sln.reverseList(listHead)

# Change the 'if' to a 'while' to print the whole list
while reversedHead is not None:
    print(reversedHead.val, end=" -> " if reversedHead.next else "")
    reversedHead = reversedHead.next

# print("Reversed head: ", reversedList.val)
# while reversedList is not None:
#     print(reversedList.val)
#     reversedList = reversedList.next
