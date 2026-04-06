"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Input: head = [0,1,2,3]

Output: [3,2,1,0]

Input: head = []

Output: []

GEMINI CHAT: https://gemini.google.com/share/8f8215d3a507
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# list ko last samma jane store the previous 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        for node in head:
            if node.next is None:

