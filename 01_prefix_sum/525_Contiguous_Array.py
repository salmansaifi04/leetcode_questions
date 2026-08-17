"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
"""


## ---------------------- brute force approach ----------------------
from typing import List
class BSolution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        for i in range(len(nums)):
            count_0 = 0
            count_1 = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    count_0 += 1
                else:
                    count_1 += 1

                if count_0 == count_1:
                    length = j - i + 1
                    max_length = max(max_length, length)
        return max_length

# Example Usage
nums = [0,1]
obj = BSolution()
print(f"Max length of contiguous subarray with equal number of 0 and 1 is: {obj.findMaxLength(nums)}") # output:2

## time complexity : O(n^2) because we are using two nested loops to calculate the count of 0s and 1s in all subarrays.
## space complexity : O(1) because we are not using any extra space.

## ---------------------- optimized approach ----------------------
class Solution:
    def findMaxlength(self, nums: List[int]) -> int:
        count_map = {0:-1} # initialize with 0 count to handle cases where the subarray starts from index 0
        count = 0
        max_length = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in count_map:
                length = i - count_map[count]
                max_length = max(max_length, length)
            else:
                count_map[count] = i

        return max_length

# Example Usage
nums = [0,1]
obj = Solution()
print(f"Max length of contiguous subarray with equal number of 0 and 1 is: {obj.findMaxlength(nums)}") # output:2

# time complexity : O(n) because we are using a single loop to calculate the count of 0s and 1s in all subarrays.
# space complexity : O(n) because we are using a dictionary to store the count of 0s and 1s in all subarrays.