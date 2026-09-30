from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def tokenizer(string: str) -> str:
            word_dict = defaultdict(int)
            for e in string:
                word_dict[e] += 1
            return word_dict
        
        convinations = defaultdict(int)
        ans = []

        for i, e in enumerate(strs):
            temp = tokenizer(e)
            if frozenset(temp.items()) not in convinations:
                convinations[frozenset(temp.items())] = len(ans)
                ans.append([e])
            else:
                 ans[convinations[frozenset(temp.items())]].append(e)
        return ans



        