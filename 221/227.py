class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        num = 0
        sign = '+'
        for i, ch in enumerate(s):
            if ch.isnumeric():
                num = num * 10 + int(ch)
            if ch in ['+', '-', '*', '/'] or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # notice : handle negative
                    # python3 version :
                    stack.append(int(stack.pop() / num))
                    # python2 version :
                    stack.append(int(stack.pop() / float(num)))
                sign = ch
                num = 0
        return sum(stack)

print(Solution().calculate("14-3/2"))
print(int(-2.3))
