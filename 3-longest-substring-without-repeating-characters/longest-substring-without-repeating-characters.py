class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        max_len = 0 
        left = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1

            char_index[ch] = right

            max_len = max(max_len, right - left + 1)

        return max_len
        