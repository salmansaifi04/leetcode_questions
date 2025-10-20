# prefix sum approach

class NumArray:
    def __init__(self, nums):
        self.prefix_sums = [0]
        for num in nums:
            self.prefix_sums.append(self.prefix_sums[-1] + num) 
        
    def sumrange(self, left, right):
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
        
# Example usage:
nums = [-2, 0, 3, -5, 2, -1]
num_array = NumArray(nums)
print(num_array.sumrange(0, 2))  # Output: 1
print(num_array.sumrange(2, 5))  # Output: -1
print(num_array.sumrange(0, 5))  # Output: -3