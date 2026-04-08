class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        finlst = [0]*n
        zero_count = nums.count(0)
        if zero_count > 1:
            return finlst
        if zero_count == 1:
            tot_prod = 1
            for num in nums:
                if num !=0:
                    tot_prod *= num
            for i in range(n):
                if nums[i] == 0:
                    finlst[i] = tot_prod
            return finlst
        left_prod = 1
        for i in range(n):
            finlst[i] = left_prod
            left_prod *= nums[i]
        right_prod = 1
        for i in range(n-1,-1,-1):
            finlst[i] *= right_prod
            right_prod *= nums[i]
        return finlst


