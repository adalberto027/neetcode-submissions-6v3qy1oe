class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            print(nums[p1:p2+1])
            m = (p1 + p2) // 2

            if nums[m] < nums[p2]:
                p2 = m
            else:
                p1 = m + 1
        print(p1,p2)
        return nums[p2]

