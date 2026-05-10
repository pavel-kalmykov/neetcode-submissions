class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = l_idx = 0
        last_seen = {}

        for r_idx, char in enumerate(s):
            if char in last_seen and last_seen[char] >= l_idx:
                l_idx = last_seen[char] + 1
            last_seen[char] = r_idx
            max_len = max(max_len, r_idx - l_idx + 1)

        return max_len