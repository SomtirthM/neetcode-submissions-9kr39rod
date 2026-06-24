class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        s_trip = "".join(char for char in lower_s if char.isalnum())
        return s_trip==s_trip[::-1]
