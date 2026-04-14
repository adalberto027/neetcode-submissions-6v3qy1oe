class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = ans = 0
        srtElements = set()

        for p2 in range(len(s)):
            if not s[p2] in srtElements:
                srtElements.add(s[p2])
            else:
                while s[p1] != s[p2]:
                    srtElements.remove(s[p1])
                    p1 += 1
                p1 += 1
            ans = max(ans, (p2 - p1) + 1)
        return ans

