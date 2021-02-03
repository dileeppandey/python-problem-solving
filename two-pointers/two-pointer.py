"""
TWO POINTER PROBLEMS
"""

"""
Easy

Remove Duplicates
    Given an array of sorted numbers remove all duplicates from it. You should not use extra space.
    After removing the duplicates return the new length of the array.

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: First four elements of the array must be [2, 3, 6, 9]
"""

from typing import List, Union

Nums = Union[int, float]

def remove_duplicates(nums: List[Nums]) -> int:
    """Given a sorted array remove duplicates in place, return new size of the array.

    Args:
        nums: List[Nums] sorted

    Returns:
        int: new size

    Raises:
        ValueError: if the list nums is empty

    >>> remove_duplicates([2, 3, 3, 3, 6, 9, 9])
    4
    """
    length = len(nums)
    if length == 0:
        raise ValueError(f'The list cannot be empty.')
    elif length == 1:
        return 1

    last_unique_at, i = 0, 0

    for i in range(1, length):
        if nums[i] == nums[i-1]:
            continue
        else:
            last_unique_at += 1
            nums[last_unique_at] = nums[i]

    return last_unique_at + 1

"""
Easy
Remove Element:
    Given an unsorted list an element, remove the element from the list in-place and return the new length of the list.

Input: [3, 2, 3, 6, 3, 10, 9, 3], k = 3
Output: 4
Explanation: The four elements must be [2, 6, 10, 9]
"""

def remove_element(nums: List[Nums], k: Nums) -> int:
    """Remove all the elements in the list nums which are equal to k, return the new size.

    Args:
        nums: List[Nums]
        k: Nums

    Returns:
        int: new size of the list

    Raises:
        ValueError: if input list nums is empty

    >>> remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)
    4
    """
    length = len(nums)
    if length == 0:
        raise ValueError(f'The input list cannot be empty.')
    next_element = 0
    for i in range(length):
        if nums[i] != k:
            nums[next_element] = nums[i]
            next_element += 1

    return next_element

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
