"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


"""

## ------------------- brute force -------------------
from typing import List
class BNumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right+1):
            total += self.nums[i]

        return total

obj = BNumArray([1,2,3,4,5])
print(f"sumRange(1, 4) : {obj.sumRange(1,4)}")

## in Brute force approach,
# __init__() takes O(1)
# sumRange() takes O(n)
# Extra space : O(1)


## ------------------- prefix sum -------------------

from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

        print(f"nums : {nums}")
        print(f"prefix : {self.prefix}")

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]

nums = [1,2,3,4,5]


# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
left = 1
right = 4
param_1 = obj.sumRange(left,right)
print(f"param_1 : {param_1}")

## in prefix sum approach,
# __init__() takes O(n)
# sumRange() takes O(1)
# Extra space : O(n)