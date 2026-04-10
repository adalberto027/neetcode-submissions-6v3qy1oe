class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}

        for e in nums:
            if e not in vals:
                vals[e] = 1
            else:
                return True
        return False
        
