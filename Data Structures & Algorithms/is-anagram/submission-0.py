class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        for e in s:
            if e not in sDict:
                sDict[e] = 1
            else:
                sDict[e] += 1

        for e in t:
            if e not in tDict:
                tDict[e] = 1
            else:
                tDict[e] += 1
        
        return tDict == sDict
        