class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(p1: int, p2: int, target: int) -> int:
            while p1 <= p2:
                m = (p1+p2)//2

                if nums[m] < target:
                    p1 = m + 1
                elif nums[m] > target:
                    p2 = m - 1
                else:
                    return m
            return -1



        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            m = (p1 + p2) // 2

            if len(nums) - 1 == p1 or p1 == p2 - 1:
                break

            if nums[p1] <= nums[m]:
                p1 = m
            else:
                p2 = m

        if target >= nums[0] and target <= nums[p1]:
            return binarySearch(0, p1, target)
        else:
            return binarySearch(p2, len(nums) - 1, target)
