class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for e in strs:
            for c in e:
                ans.append(str(ord(c)))
                ans.append(',')
            ans.append('#')
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        ans = s.split('#')
        ans.pop()
        for i in range(len(ans)):
            ans[i] = ans[i].split(',')
            ans[i].pop()

        for i in range(len(ans)):
            for j in range(len(ans[i])):
                ans[i][j] = chr(int(ans[i][j]))
            ans[i] = ''.join(ans[i])
        return ans