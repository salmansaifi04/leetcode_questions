"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

"""

## --------------- brute force approach -----------------
from typing import List
class BSolution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        return -1


# example usage
nums = [1,7,3,6,5,6]
obj = BSolution()
print(f"Pivot index is: {obj.pivotIndex(nums)}") # Output:3

nums1 = [1,2,3]
print(f"Pivot index is: {obj.pivotIndex(nums1)}") # Output:-1

# time complexity: O(n^2) because for each index we are calculating the sum of left and right subarrays which takes O(n) time.
# space complexity: O(1) because we are not using any extra space.


## --------------- optimized approach -----------------
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1

obj = Solution()
print(f"Pivot index is: {obj.pivotIndex(nums)}") # output:3
print(f"Pivot index is: {obj.pivotIndex(nums1)}") # output:-1

# time complexity: O(n) because we are calculating the total sum of the array in O(n) time and then iterating through the array once which takes O(n) time.
# space complexity: O(1) because we are not using any extra space.