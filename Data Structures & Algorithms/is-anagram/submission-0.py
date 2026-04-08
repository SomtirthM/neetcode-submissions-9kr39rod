class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()
        s_sort = sorted(s)
        t_sort = sorted(t)
        if len(s_sort) == len(t_sort):
            if s_sort == t_sort:
                return True
        return False