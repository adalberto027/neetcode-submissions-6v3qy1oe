class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            m = (p1 + p2) // 2

            if nums[p2] > nums[m]:
                p2 = m 
            else:
                p1 = m + 1 
                

        return nums[p2]
