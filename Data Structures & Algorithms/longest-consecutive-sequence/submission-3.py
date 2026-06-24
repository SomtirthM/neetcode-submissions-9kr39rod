class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        if not nums: return 0
        for ele in nums:
            curr = ele 
            max_len = 0
            while curr in num_set:
                max_len += 1
                curr += 1
            count = max(count, max_len)
        return count

        