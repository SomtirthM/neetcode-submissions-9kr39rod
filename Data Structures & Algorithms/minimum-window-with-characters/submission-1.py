class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1
        required = len(t_freq)
        left = 0
        formed = 0
        win_freq = {}
        min_len = float('inf')
        res_left = 0
        for right in range(len(s)):
            ch = s[right]
            win_freq[ch] = win_freq.get(ch, 0) + 1
            if ch in t_freq and win_freq[ch] == t_freq[ch]:
                formed += 1
            while formed == required:
                win_len = right - left + 1
                if win_len < min_len:
                    min_len = win_len
                    res_left = left
                left_char = s[left]
                win_freq[left_char] -= 1
                if(left_char in t_freq and win_freq[left_char] < t_freq[left_char]):
                    formed -= 1
                left += 1
        if min_len == float('inf'):
            return ""
        return s[res_left: res_left+min_len]

