class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        L, R= 0, len(height) - 1
        max_L, max_R = height[L], height[R]
        ans = 0

        while L < R:
            if max_L <= max_R:
                L += 1
                max_L = max(max_L, height[L])
                ans += max_L - height[L]
            else:
                R -= 1
                max_R = max(max_R, height[R])
                ans += max_R - height[R]
        return ans


