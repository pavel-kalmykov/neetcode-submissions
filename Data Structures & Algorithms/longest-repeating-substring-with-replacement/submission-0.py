class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_freq_count = l_idx = 0
        char_count_window = {}

        for r_idx, char in enumerate(s):
            char_count_window[char] = char_count_window.get(char, 0) + 1
            most_freq_count = max(most_freq_count, char_count_window[char])

            if r_idx - l_idx + 1 - most_freq_count > k:
                char_count_window[s[l_idx]] -= 1
                l_idx += 1

        return r_idx - l_idx + 1