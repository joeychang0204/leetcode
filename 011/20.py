class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i, ch in enumerate(s):
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not queue:
                    return False
                if (ch == '}' and stack[-1] != '{' ) or (ch == ']' and stack[-1] != '[' ) or (ch == ')' and stack[-1] != '(' ):
                    return False
                stack.pop(-1)
        if stack:
            return False
        return True
