"""
Given a sorted array of numbers find if a given number key is present in the array.
Array can be ordered in ascending or descending order.

Example:
    Input: [1,2,3,4,5], k = 3
    Output: 2

    Input: [10, 8, 6, 5, 3, 2], k = 3
    Output: 4
"""
from typing import List, Union

Num = Union[int, float]

def binary_search(arr: List[Num], k: Num) -> int:
    """ Returns index of the key if it exists orherwise -1
        Assumption:
            Array is in ascending order
    """
    start = 0
    end = len(arr) - 1
    is_ascending = False

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == k:
            return mid
        if is_ascending:
            if arr[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] > k:
                start = mid + 1
            else:
                end = mid - 1
    return -1

if __name__ == "__main__":
    print(f"Index if 3 in [1,2,3,4,5] is: {binary_search([1,2,3,4,5], 3)}")
    print(f"Index if 3 in [10, 8, 6, 5, 3, 2] is: {binary_search([10, 8, 6, 5, 3, 2], 3)}")
    print(f"Index if 3 in [10, 8, 6, 3, 3, 2] is: {binary_search([10, 8, 6, 3, 3, 2], 3)}")

"""
Discuss:
    Time Complexity: O(logn)
    Space Complexity: O(1)

    Modify binary search to handle cases for ascending and descending array.

    This solution does not guarantee index of first occurrence of k.

"""

