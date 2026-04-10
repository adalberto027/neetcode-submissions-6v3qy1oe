class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, e in enumerate(nums):
            numsDict[e] = i

        for i, e in enumerate(nums):
            if (target - e) in numsDict and (i is not numsDict[(target - e)]):
                return [i, numsDict[(target - e)]]