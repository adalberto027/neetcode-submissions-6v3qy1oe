from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        count = defaultdict(int)

        for e in nums:
            count[e] += 1
        
        sort = []

        for i in range(len(nums) + 1):
            sort.append([])
        for z, v in count.items():
            sort[v].append(z)

        ans = []

        for i, e in enumerate(reversed(sort)):
            if len(ans) < k:
                ans += e
            else:
                return ans
        return ans