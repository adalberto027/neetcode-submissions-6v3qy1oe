class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        ans = set()

        for p1 in range(len(nums)-2):
            missing = -nums[p1]
            p2, p3 = (p1 + 1), (len(nums)-1)

            while p2 < p3:
                if nums[p2] + nums[p3] > missing:
                    p3 -= 1
                elif nums[p2] + nums[p3] < missing:
                    p2 += 1
                else:
                    ans.add((nums[p1],nums[p2],nums[p3]))
                    p2 += 1
        
        return list(ans)
