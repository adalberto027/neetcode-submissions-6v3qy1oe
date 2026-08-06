class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_elements = set(nums)
        ans = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in nums_elements:
                temp = 1
                t = 1
                while nums[i] + t in nums_elements:
                    temp += 1
                    t += 1
                ans = max(ans, temp)

        return ans
            
                
        