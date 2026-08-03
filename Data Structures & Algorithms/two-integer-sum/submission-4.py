class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_index = {}
        for i in range(len(nums)):
            if (target - nums[i]) in seen_index:
                return [seen_index[(target - nums[i])], i]
            seen_index[nums[i]] = i
        