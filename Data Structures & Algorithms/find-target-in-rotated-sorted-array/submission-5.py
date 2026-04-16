class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(n: List[int], t: int, s = 0, e = len(nums) - 1):
            l , r = s , e

            while l <= r:
                m = (l + r) // 2
                if nums[m] > t:
                    r = m - 1
                elif nums[m] < t:
                    l = m + 1
                else:
                    return m
            return -1

        i = l = 0
        r = len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] <= nums[i]:
                    i = l
                break
            
            m = (l + r) // 2
            if nums[m] <= nums[i]:
                i = m 
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        if target > nums[-1]:
            return binarySearch(nums, target, e = i)
        else:
            return binarySearch(nums, target, s = i)