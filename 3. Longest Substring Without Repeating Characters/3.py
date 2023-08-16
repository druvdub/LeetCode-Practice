class Solution:

    '''

    Sliding Window Approach

    Time Complexity: O(n)
    Space Complexity: O(n)

    '''

    def lengthOfLongestSubstring(self, s: str) -> int:
        best = left = 0
        seen = {}
        for right, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char] + 1)
            seen[char] = right
            best = max(best, right - left + 1)
        return best

    def lengthOfLongestSubstring2(self, s: str) -> int:
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length
