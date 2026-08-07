class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = float('INF')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_ = min(val, self.min_)

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min_ =  min(self.stack)
        else:
            self.min_ = float('INF')   

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_
        
