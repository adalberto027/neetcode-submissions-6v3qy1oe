class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*','/'}

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                first =stack.pop()
                second = stack.pop()
                
                if tokens[i] == '+':
                    stack.append(int(second) + int(first))
                elif tokens[i] == '-':
                    stack.append(int(second) - int(first))
                elif tokens[i] == '*':
                    stack.append(int(second) * int(first))
                elif tokens[i] == '/':
                    stack.append(int(int(second) / int(first)))

        return int(stack.pop())
