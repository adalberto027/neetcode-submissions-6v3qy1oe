class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for e in strs:
            ans += str(len(e)) + '#' + e
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0
        j = 0


        while i < len(s):
            if s == '':
                return ['']
            l = ''
            while s[j] != '#':
                l += s[j]
                j += 1
            ans += [s[j+1: j+1+int(l)]]
            j += int(l) + 1
            i = j
        return ans
