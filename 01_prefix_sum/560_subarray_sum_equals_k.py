"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""


## --------------- brute force approach -----------------
from typing import List
class BSolution:
    def subarraySum(self, nums: List[int], k:int) -> int:
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]

                if sum == k:
                    count += 1

        return count

# Example Usage
nums = [1,1,1]
k = 2
obj = BSolution()
print(obj.subarraySum(nums, k))


nums1 = [1,2,3]
k1 = 3
print(obj.subarraySum(nums1, k1))

# time complexity : O(n^2) because we are using two nested loops to calculate the sum of all subarrays.
# space complexity : O(1) because we are not using any extra space.


## ------------- optimized approach -----------------
class Solution:
    def subarraySum(self, nums: List[int], k:int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_map = {0:1} # initialize with 0 sum to handle cases where the subarray starts from index 0

        for num in nums:
            prefix_sum += num

            # check if there is a prefix sum that when subtracted from the current prefix sum equals k
            if (prefix_sum - k) in prefix_sum_map:
                count += prefix_sum_map[prefix_sum - k]

            # update the prefix sum map with the current prefix sum
            if prefix_sum in prefix_sum_map:
                prefix_sum_map[prefix_sum] += 1
            else:
                prefix_sum_map[prefix_sum] = 1

        return count

# Example Usage
nums = [1,1,1]
k = 2
obj = Solution()
print(obj.subarraySum(nums, k)) # output : 2

print(obj.subarraySum([1,2,3], 3)) # output : 2


# time complexity : O(n) because we are traversing the array only once.
# space complexity : O(n) because we are using a hashmap to store the prefix sums.

