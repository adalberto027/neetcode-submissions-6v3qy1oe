class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        seen = {}
        ans = set()
        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums)):
                if -(nums[j] + nums[i]) in seen:
                    sor = sorted([nums[j], nums[i], -(nums[j] + nums[i])])
                    ans.add((sor[0],sor[1],sor[2]))
                seen[nums[j]] = j
            seen = {}
        return list(ans)
        