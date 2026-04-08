class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        #Key: sorted_strs & Value: list of strings that match
        for s in strs:
            sorted_strs = ''.join(sorted(s))
            if sorted_strs not in anagrams:
                anagrams[sorted_strs]=[s]
            else:
                anagrams[sorted_strs].append(s)
        return anagrams.values()

