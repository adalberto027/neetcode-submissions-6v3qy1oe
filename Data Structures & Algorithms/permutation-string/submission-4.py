class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p1 = 0

        s1Dict = {}
        for e in s1:
            if e not in s1Dict:
                s1Dict[e] = 1
            else:
                s1Dict[e] += 1

        cur = {}
        for p2 in range(len(s2)):
            print(1)
            if p2 < len(s1):
                if s2[p2] not in cur:
                    cur[s2[p2]] = 1
                else:
                    cur[s2[p2]] += 1
            else:
                cur[s2[p1]] -= 1

                if cur[s2[p1]] == 0:
                    del cur[s2[p1]]
                p1 += 1

                if s2[p2] not in cur:
                    cur[s2[p2]] = 1
                else:
                    cur[s2[p2]] += 1
            if s1Dict == cur:
                return True
        return False                


        