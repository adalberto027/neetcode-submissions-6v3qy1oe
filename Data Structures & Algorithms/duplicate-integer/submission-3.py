class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = set()

        for e in nums:
            if e in elements:
                return True
            elements.add(e)
        return False
        