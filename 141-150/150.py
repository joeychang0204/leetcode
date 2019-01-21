class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "-":
                    stack.append(num1 - num2)
                elif t == "*":
                    stack.append(num1 * num2)
                else:
                    if num1 * num2 < 0:
                        stack.append(int(abs(num1)/abs(num2)) * (-1))
                    else:
                        stack.append(int(num1/num2))
            else:
                stack.append(int(t))
        return stack[-1]

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
