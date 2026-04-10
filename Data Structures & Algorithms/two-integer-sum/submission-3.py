class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, e in enumerate(nums):
            if (target - e) in numsDict and (i is not numsDict[(target - e)]):
                return [numsDict[(target - e)], i]
            numsDict[e] = i
        #Space and time complexity is O(n) 