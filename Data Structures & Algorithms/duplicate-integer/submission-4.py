class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for ele in nums:
            if ele in seen:
                return True 
            else:
                seen.add(ele)
        return False
        