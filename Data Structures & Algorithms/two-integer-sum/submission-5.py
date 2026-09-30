from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)

        for i, e in enumerate(nums):
            if target - e in dic:
                return [dic[target - e], i]
            dic[e] = i
        