class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ldt = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ldt.append(i)
                    ldt.append(j)
        return ldt
                    
