class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        ans = 0
        while p1 < p2:
            ans = max(ans, ((p2 - p1) * min(heights[p1],heights[p2])))
            if heights[p1] >= heights[p2]:
                p2 -= 1
            else:
                p1 += 1
        return ans
        