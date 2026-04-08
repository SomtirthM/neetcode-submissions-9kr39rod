class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        freq_list = [(key, count) for key, count in freq.items()]
        freq_list.sort(key=lambda x:x[1], reverse=True)
        top_k = [item[0] for item in freq_list[:k]]
        return top_k
