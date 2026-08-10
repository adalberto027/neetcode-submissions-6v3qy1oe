class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p1 = 1
        p2 = max(piles)
        ans = p2

        while p1 <= p2:

            m = (p1 + p2) // 2
            count = 0
            print(m)

            for e in piles:
                count += (e // m) 
                if e % m != 0:
                    count += 1

            print(count < h, abs(count - h) < abs(ans - h), abs(count - h), abs(ans - h))


            if count <= h:
                ans = m
                p2 = m - 1
            elif count - h > 0:
                p1 = m + 1
        return ans
