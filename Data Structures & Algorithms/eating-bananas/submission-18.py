class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            count = 0

            for e in piles:
                temp = e // m
                count += temp
                if e % m :
                    count += 1
                
            if count <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
            
                