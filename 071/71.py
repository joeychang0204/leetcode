class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split('/')
        stack = []
        for d in dirs:
            if d == '..' and stack:
                stack.pop()
            elif d != '.' and d != '..' and d:
                stack.append(d)
        return '/' + '/'.join(stack)
        
