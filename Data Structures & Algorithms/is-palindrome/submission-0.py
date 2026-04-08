class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_apn = ''.join(char for char in s if char.isalnum()).lower()
        rev_str = s_apn[::-1]
        if rev_str == s_apn:
            return True
        else:
            return False