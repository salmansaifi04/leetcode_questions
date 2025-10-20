def find_max_length(nums):
    count_index_map = {0: -1}
    max_length = 0
    count = 0
    
    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        print("i : ", i, " num : ", num, " count : ", count, " max_length : ", max_length, " count_index_map : ", count_index_map)

        if count in count_index_map:
            max_length = max(max_length, i - count_index_map[count])
        else:
            count_index_map[count] = i

    print("count_index_map : ", count_index_map)
    return max_length


# Example usage:
nums = [0, 1, 0, 1, 0, 1, 1]
print(find_max_length(nums)) # Output: 6