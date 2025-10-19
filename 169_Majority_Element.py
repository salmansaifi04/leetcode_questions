# Majority Element using Hash Map 
def majprityElement_by_using_hash_map(nums):
    nums_count = {}
    for num in nums:
        nums_count[num] = nums_count.get(num, 0) + 1
    
    for num, count in nums_count.items():
        if count > len(nums) // 2:
            return num
    
# Example usage:
nums = [3, 2, 3]
majprityElement_by_using_hash_map(nums)  # Output: 3
print(majprityElement_by_using_hash_map(nums))



# Majority Element using Boyer-Moore Voting Algorithm
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# Example usage:
nums = [2, 2, 2, 2, 1, 1, 1, 1, 2]
majorityElement(nums)  # Output: 2
print(majorityElement(nums))