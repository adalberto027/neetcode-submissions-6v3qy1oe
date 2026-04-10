class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = {}
        ans = []

        for i, e in enumerate(strs):
            temp = {}
            for j, e2 in enumerate(e):
                if e2 not in temp:
                    temp[e2] = 1
                else:
                    temp[e2] += 1
            if frozenset(temp.items()) not in anagramsMap:
                anagramsMap[frozenset(temp.items())] = len(anagramsMap.values())
                ans += [[e]]
            else:
                ans[anagramsMap[frozenset(temp.items())]] += [e]
        return ans



        