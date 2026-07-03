class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_values = [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
        return max_values