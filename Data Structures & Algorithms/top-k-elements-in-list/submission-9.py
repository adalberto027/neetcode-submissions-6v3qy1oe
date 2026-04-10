class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for e in nums:
            if e not in dic:
                dic[e] = 1
            else:
                dic[e] += 1
        inversDict = {}
        for key, v in dic.items():
            if v not in inversDict:
                inversDict[v] = [key]
            else:
                inversDict[v] += [key]
        
        helper = sorted(list(inversDict.keys()))

        ans = []
        print(k)
        for e in reversed(helper):
            ans += inversDict[e]

        print(k)

        return ans[:k]

        