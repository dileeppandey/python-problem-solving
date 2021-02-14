"""
SLIDING WINDOW PROBLEMS
"""

"""
Easy
Given an array, find the average of all contiguous subarrays of size 'K' in it.

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K = 5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""

from typing import List, Union

Nums = Union[int, float]

def find_average_of_subarrays_brute(nums: List[Nums], k:int) -> List[Nums]:
    """Given an array, find the average of all subarrays of size 'k'

    Args:
        nums: List[Nums]
        k: int

    Returns:
        List[Nums]

    Raises:
        ValueError: if k <= 0 or nums is empty
    """
    length = len(nums)
    if k <= 0:
        raise ValueError(f'{k} is not greater than 0.')
    if length == 0:
        raise ValueError('List nums cannot be empty.')
    if k > length:
        raise ValueError(f'{k} is greater than the size of input list.')

    averages = []
    for i in range(length-k+1):
        averages.append(sum(nums[i:i+k]) / k)

    return averages


def find_average_of_subarrays_sw(nums: List[Nums], k:int) -> List[Nums]:
    """Given an array, find the average of all subarrays of size 'k'

    Args:
        nums: List[Nums]
        k: int

    Returns:
        List[Nums]

    Raises:
        ValueError: if k <= 0 or nums is empty
    """
    length = len(nums)
    if k <= 0:
        raise ValueError(f'{k} is not greater than 0.')
    if length == 0:
        raise ValueError('List nums cannot be empty.')
    if k > length:
        raise ValueError(f'{k} is greater than the size of input list.')

    averages = []
    window_start, window_end, windows_sum = 0, 0, 0

    for window_end in range(length):
        window_sum += nums[window_end]

        if window_end >= k - 1:
            avaerage = window_sum / k
            averages.append(average)
            window_sum -= nums[window_start]
            window_start += 1

    return averages

"""
Easy
Maximum Sum Subarray of Size K

Input: [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: [5, 1, 3]
"""

"""
Brute Force:

Use two nested loops to keep track of maximum of last k elements of the array
"""
def find_max_subarray_sum_brute(nums: List[Nums], k: int) -> Nums:
    """Given a list of numbers, find the maximum subarray sum of size k

    Args:
        nums: List[Nums]
        k: int

    Returns:
        Nums

    Raises:
        ValueError if k < 0 or k > length of nums or nums is empty
    """
    length = 0
    if length == 0:
        raise ValueError(f'The input list nums cannot be empty.')
    if k <= 0:
        raise ValueError(f'The value of k must be greater than 0.')
    if k > length:
        raise ValueError(f'k must not be greater than the size of input list nums')

    max_sum = float('-Inf')
    for i in range(length-k+1):
        max_sum = max(sum(nums[i:i+k]), max_sum)

    return max_sum

def find_max_subarray_sum_sw(nums: List[Nums], k: int) -> Nums:
    """Given a list of numbers, find the maximum subarray sum of size k

    Args:
        nums: List[Nums]
        k: int

    Returns:
        Nums

    Raises:
        ValueError if k < 0 or k > length of nums or nums is empty
    """
    length = 0
    if length == 0:
        raise ValueError(f'The input list nums cannot be empty.')
    if k <= 0:
        raise ValueError(f'The value of k must be greater than 0.')
    if k > length:
        raise ValueError(f'k must not be greater than the size of input list nums')

    window_start, window_end, max_sum = 0, 0, float('-Inf')

    for window_end in range(length):
        window_sum += nums[window_end]

        if window_end >= k - 1:
            max_sum = max(window_sum, max_sum)
            window_sum -= nums[window_start]
            window_start += 1

    return max_sum

"""
Easy
Smallest Subarray with a given sum

Input: [2, 1, 5, 2, 3, 2], S = 7
Output: 2
Explanation: [5, 2] is the smallest subarray that sums to 7
"""

def find_smallest_subarray_sum_brute(nums: List[Nums], s: Nums) -> int:
    """Given an array of numbers and int k find the size of smallest contiguous subarray that sums to s

    Args:
        nums: List[Nums]
        s: Nums

    Returns:
        int: size of subarray if it is found else return -1

    Raises:
        ValueError: if nums is empty
    """
    length = len(nums)
    if length == 0:
        raise ValueError(f'The input list cannot be empty.')

    smallest_size = float('Inf')

    for i in range(length):
        j = i
        current_sum = 0
        while j < length and current_sum <= s:
            current_sum += nums[j]
            j += 1
        if current_sum == s:
            smallest_size = min(smallest_size, j - i)

    return -1 if smallest_size > length else smallest_size

def find_smallest_subarray_sum_sw(nums: List[Nums], s: Nums) -> int:
    """Given an array of numbers and int k find the size of smallest contiguous subarray that sums to s

    Args:
        nums: List[Nums]
        s: Nums

    Returns:
        int: size of subarray if it is found else return -1

    Raises:
        ValueError: if nums is empty
    """
    length = len(nums)
    if length == 0:
        raise ValueError(f'The input list cannot be empty.')

    window_start, window_end, window_sum, smallest_size =. 0, 0, 0, float('Inf')

    for window_end in range(length):
        window_sum += nums[window_end]

        if window_sum < s:
            continue
        elif window_sim == s:
            smallest_size = min(smallest_size, window_end - window_start + 1)
        else:
            while window_sum > s:
                window_sum -= nums[window_start]
                window_start += 1

    return -1 if smallest_size > length else smallest_size


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
