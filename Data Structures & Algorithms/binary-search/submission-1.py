class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        flg = []
        for i in range(n):
            if nums[i] == target:
                flg.append(i)
        if len(flg) == 1:
            return flg[0]
        elif len(flg) > 1:
            for i in range(len(flg)):
                return flg[i]
        else:
            return -1
            