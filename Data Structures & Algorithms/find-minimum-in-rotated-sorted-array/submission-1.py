class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1, p2 = 0, len(nums) - 1

        while p1 < p2:
            m  = (p1 + p2) // 2
            if nums[p1] > nums[p2]:
                if nums[p1] >= nums[m]:
                    p2 = m
                else:
                    p1 = m
            else:
                p2 = m

        if not len(nums) > p1+1:
            return nums[p1]
        else:
            return min(nums[p1], nums[p1+1])
        