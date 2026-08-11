"""
There is a biker going on a road trip. The road trip consists of n + 1 points at various altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

"""

## --------------- brute force approach -----------------
from typing import List
class BSolution:
    def LargestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        for i in range(len(gain)+1):
            altitude = 0
            for j in range(i):
                altitude += gain[j]

            highest_altitude = max(highest_altitude, altitude)

        return highest_altitude

# example usage:
gain = [-5,1,5,0,-7]
obj = BSolution()
print(f"Highest altitude is: {obj.LargestAltitude(gain)}") # output:1

gain1 = [-4,-3,-2,-1,4,3,2]
print(f"Highest altitude is: {obj.LargestAltitude(gain1)}") # output:0


# time complexity: O(n^2) because for each index we are calculating the sum of the gain array which takes O(n) time.
# space complexity: O(1) beacuse we are not using any extra space.


## -------------- optimized approach -----------------
class Solution:
    def LargestAltitude(self, gain: List[int]) -> int:
        prefix = [0]
        for g in gain:
            prefix.append(prefix[-1] + g)
        return max(prefix)

        # highest = 0
        # current = 0
        # for change in gain:
        #     current += change
        #     highest = max(highest, current)
        
        # return highest
        
# example usage:
obj = Solution()
print(f"Highest altitude is: {obj.LargestAltitude(gain)}") # output:1
print(f"Highest altitude is: {obj.LargestAltitude(gain1)}") # output:0

# time complexity: O(n) because we are calculating the prefix sum of the gain array which takes O(n) time.
# space Complexity: O(n) because we are using an extra array to store the prefix sum of the gain array.