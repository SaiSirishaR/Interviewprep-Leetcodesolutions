from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        group_anagram = []

        for word in strs:
            sorted_charc = tuple(sorted(word))
            d[sorted_charc].append(word)
        
        return d.values()
