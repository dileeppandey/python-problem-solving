"""
Write a function that takes a non-negative integer and returns
the largest integer whose square is less than or equal to the 
integer given.

Example:
    input: 150
    output: 12

    12 ** 2 = 144, 13 ** 2 = 169, hence the answer is 12.
"""

def get_integer_square_root(num: int) -> int:
    if num == 0 or num == 1:
        return num
    low = 0
    high = num
    while low <= high:
        mid = low + (high - low) // 2
        squared = mid ** 2
        if squared <= num:
            low = mid + 1
        else:
            high = mid - 1

    return low - 1

if __name__ == "__main__":
    print("Resule is: ", get_integer_square_root(26))
    print("Result is: ", get_integer_square_root(150))

"""
Discuss:
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Use binary search approach to shorten the search space in half.
"""

