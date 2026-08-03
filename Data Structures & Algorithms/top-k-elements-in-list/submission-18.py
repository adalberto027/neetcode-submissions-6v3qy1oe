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
        
        print(sort)

        ans = []

        for i, e in enumerate(reversed(sort)):
            print(len(ans), k)
            if len(ans) < k:
                ans += e
            else:
                return ans
            print(ans)
        print(sort)
        return ans