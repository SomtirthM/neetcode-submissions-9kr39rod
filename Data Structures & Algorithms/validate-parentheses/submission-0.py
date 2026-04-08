class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in bracket_dict:
                top_element = stack.pop() if stack else '#'
                if bracket_dict[char] != top_element:
                    return False
            else:
                stack.append(char)
            
        return not stack
