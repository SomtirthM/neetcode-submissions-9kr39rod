class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:    
                count[num] = 1
        count_sorted = sorted(count.items(), key = lambda x:x[1], reverse=True)
        for num, freq in count_sorted[:k]:
            result.append(num)
        return result
