from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagr_map = defaultdict(list)
        for e in strs:
            anagr_map[''.join(sorted(e))].append(e)
        return list(anagr_map.values())