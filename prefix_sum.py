def prefix_sum(arr):
    """
    Calculate the prefix sum of a given list of numbers.

    :param arr: List of numbers
    :return: List of prefix sums
    """
    for i in range(len(arr)):
        if i > 0:
            arr[i] += arr[i - 1]
    return arr

# Example usage:
arr = [1, 2, 3, 4]
print(prefix_sum(arr))  # Output: [1, 3, 6, 10]
