from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            counts = Counter(word)
            key = frozenset(counts.items())
            hash_map[key].append(word)
        return list(hash_map.values())
            

        