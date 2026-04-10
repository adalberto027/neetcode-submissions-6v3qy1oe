class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setElemnts = set(nums)
        longest = 0

        for e in nums:
            length = 1
            if (e - 1) not in setElemnts:
                while (e + 1) in setElemnts:
                    length += 1
                    e += 1
            longest = max(longest, length)
        return longest