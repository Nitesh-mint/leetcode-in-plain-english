"""
Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

    constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
    int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.


Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

Output:
[null, 3, 3, 3, 5, 6]

Explanation:
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3);   // return 3
kthLargest.add(5);   // return 3
kthLargest.add(6);   // return 3
kthLargest.add(7);   // return 5
kthLargest.add(8);   // return 6
"""

# We are using min-heap to solve this.

import heapq
import math
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        heapq.heapify(self.nums)  # conver to  heap (defaults to min-heap)

        # only keep the k largest elements
        # [1, 2,3, 4, 5, 6] k = 3 --> keep [4, 5, 6]
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
