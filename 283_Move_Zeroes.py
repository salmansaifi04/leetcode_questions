def moveZeroes(nums):
    """
    Move all zeros in the list 'nums' to the end while maintaining the relative order of non-zero elements.
    
    :param nums: List[int] - List of integers
    :return: None - The function modifies the list in place
    """
    last_non_zero_index = 0

    # Move all non-zero elements to the front of the list
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_index], nums[i] = nums[i], nums[last_non_zero_index]
            last_non_zero_index += 1

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]