from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = defaultdict(int)

        for e in nums:
            elements[e] += 1
        rank = []
        for o, v in elements.items():
            rank.append((v,o))
        ans = []
        for v, o in sorted(rank,reverse = True):
            if k <= 0:
                break 
            k -= 1
            ans.append(o)
        return ans


        
        