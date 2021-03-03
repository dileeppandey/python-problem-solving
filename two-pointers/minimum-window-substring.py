"""Given two strings s and t, find the minimum window in s that contains all the characters from t. Order is not important.

Input:      "ADOBEBANC", "ABC"
Output:     "BANC"
"""

from collections import Counter, defaultdict, namedtuple

def minimum_window_substring(s: str, t: str) -> int:
    """

    Sliding Window Approach:

    * Count the char frequency in t
    * Start end pointer from left of s, and moving it to the right
        * if found a char from t, track it
        * if all of chars found
            * check with other candidates if this window is smaller one than the candidate
            * Move start pointer to the right

    Tests:
    >>> minimum_window_substring( "ADOBEBANC", "ABC")
    'BANC'
    """

    char_freq_t = Counter(t)
    start, end = 0, 0
    formed = 0
    required_unique_char_count = len(char_freq_t)
    candidate = namedtuple('candidate', 'length start end')
    ans = candidate(float('inf'), -1, -1)
    window_char_freq = defaultdict(int)

    while end < len(s):

        character = s[end]
        window_char_freq[character] += 1
        if character in char_freq_t and window_char_freq[character] == char_freq_t[character]:
            formed += 1

        # Contract Window from left
        while start <= end and formed == required_unique_char_count:
            character = s[start]

            if end - start + 1 < ans[0]:
                ans = candidate(end-start+1, start, end)

            window_char_freq[character] -= 1

            if character in char_freq_t and window_char_freq[character] < char_freq_t[character]:
                formed -= 1

            start += 1

        # Expand window on the right
        end += 1

    return "" if ans[0] == float('inf') else s[ans.start: ans.end+1]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
