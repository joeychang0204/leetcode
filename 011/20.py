class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        for i, ch in enumerate(s):
            if ch in ['(', '[', '{']:
                queue.append(ch)
            else:
                if not queue:
                    return False
                if (ch == '}' and queue[-1] != '{' ) or (ch == ']' and queue[-1] != '[' ) or (ch == ')' and queue[-1] != '(' ):
                    return False
                queue.pop(-1)
        if queue:
            return False
        return True
