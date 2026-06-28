class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = [0]*26
        win_freq = [0]*26
        m = len(s1)
        for i in range(m):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')
            s1_freq[idx1] += 1
            win_freq[idx2] += 1
        if s1_freq == win_freq:
            return True
        for right in range(m, len(s2)):
            outgoing = ord(s2[right-m]) - ord('a')
            incoming = ord(s2[right]) - ord('a')
            win_freq[outgoing] -= 1
            win_freq[incoming] += 1
            if s1_freq == win_freq:
                return True
        return False