class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1, p2 = 0, len(nums)-1

        while p1 <= p2:
            m = int((p1 + p2)/2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                p2 = m - 1
            else:
                p1 = m + 1
        return -1