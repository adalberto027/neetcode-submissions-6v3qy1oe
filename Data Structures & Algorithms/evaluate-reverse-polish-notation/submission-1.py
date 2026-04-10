class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+','-','*','/'}
        stack = []

        for e in tokens:
            if e in operators:
                pop1 = stack.pop()
                pop2 = stack.pop()
                temp = int(eval(str(pop2) + str(e) + str(pop1)))
                stack.append(temp)
            else:
                stack.append(e)
        return int(stack.pop())
