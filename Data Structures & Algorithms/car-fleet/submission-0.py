class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        positionAndSpeed = {}

        for i in range(len(position)):
            if position[i] not in positionAndSpeed:
                positionAndSpeed[position[i]] = [speed[i]]
            else:
                positionAndSpeed[position[i]] += [speed[i]]


        sortedpostions = sorted(positionAndSpeed.keys(), reverse=True)

        s = []
        for e in sortedpostions:
            for el in positionAndSpeed[e]:
                if (s and (((target-e)/el) > s[-1])) or (not s):
                    s.append((target-e)/el)
        return len(s)



        