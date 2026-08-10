class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p1 = 1
        p2 = max(piles)
        ans = p2

        while p1 <= p2:

            m = (p1 + p2) // 2
            count = 0
            for e in piles:
                count += (e // m) 
                if e % m != 0:
                    count += 1

            if count <= h:
                ans = m
                p2 = m - 1
            else:
                p1 = m + 1
        return ans
