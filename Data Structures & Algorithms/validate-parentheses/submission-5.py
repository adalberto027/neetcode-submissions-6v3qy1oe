class Solution:
    def isValid(self, s: str) -> bool:
        S = []
        options = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for e in s:
            if S and S[-1] in options and e == options[S[-1]]:
                S.pop()
            else:
                S.append(e)
        return len(S) == 0
        