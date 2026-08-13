"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0

"""

## --------------- brute force approach -----------------
from typing import List
class BSolution:
    def subarraysDivByK(self, nums: List[int], k:int) -> int:
        count = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]

                if current_sum % k == 0:
                    count += 1

        return count


# Example Usage
nums = [4,5,0,-2,-3,1]
k = 5
obj = BSolution()
print(obj.subarraysDivByK(nums, k))

# time complexity : O(n^2) because we are using two nested loops to calculate the sum of all subarrays.
# space complexity : O(1) because we are not using any extra space.


## ------------- optimized approach -----------------
class Solution:
    def subarraysDivByK(self, nums: List[int], k:int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_map = {0:1} # initialize with 0 sum to handle cases where the subarray starts from index 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k

            if mod < 0:  # handle negative mod values
                mod += k

            # check if there is a prefix sum that when subtracted from the current prefix sum gives a sum divisible by k
            if mod in prefix_sum_map:
                count += prefix_sum_map[mod]

            # update the prefix sum map
            prefix_sum_map[mod] = prefix_sum_map.get(mod, 0) + 1

        return count

# Example Usage
nums = [4,5,0,-2,-3,1]
k = 5
obj = Solution()
print(obj.subarraysDivByK(nums, k))

# time complexity : O(n) because we are using a single loop to calculate the prefix sum and check for the count of subarrays.
# space complexity : O(k) because we are using a hashmap to store the count of prefix