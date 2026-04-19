class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dic:
            self.dic[key] = [('', 0), (value, timestamp)]
        else:
            self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ''
        values = self.dic[key]
        p1, p2 = 0, len(self.dic[key])-1

        while p1 <= p2:
            m = (p1 + p2) // 2
            if values[m][1] > timestamp:
                p2 = m - 1
            elif values[m][1] < timestamp:
                p1 = m + 1
            else:
                return values[m][0]
        return values[p2][0]
        
