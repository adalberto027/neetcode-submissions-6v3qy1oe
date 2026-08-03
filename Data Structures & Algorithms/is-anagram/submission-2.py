from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1
        
        return s_dict == t_dict