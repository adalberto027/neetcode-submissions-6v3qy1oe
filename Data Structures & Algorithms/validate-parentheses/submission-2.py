class Solution:
    def isValid(self, s: str) -> bool:

        operators = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        temp = []

        for i in range(len(s)-1, -1, -1):
            if temp:
                if temp[-1] not in operators:
                    temp += [s[i]]
                elif operators[temp[-1]] == s[i]:
                    temp.pop()
                else:
                    temp += [s[i]]
            else:
                temp += [s[i]]

        return not temp