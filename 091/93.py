class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(1,4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    n1, n2, n3, n4 = s[:i],s[i:j], s[j:k], s[k:]
                    inValid = False
                    for n in [n1, n2, n3, n4]:
                        if not n or (n[0] == '0' and len(n) > 1):
                            inValid = True
                            break
                    if inValid:
                        continue
                            
                    if int(n1)<=255 and int(n2)<=255 and int(n3)<=255 and int(n4) <= 255:
                        res.append(n1+'.'+n2+'.'+n3+'.'+n4)
        return res
    def restoreIpAddresses2(self, s: str) -> List[str]:
        self.res = []
        def dfs(seperated, remain, cur):
            if seperated == 4:
                if not remain:
                    # remove the last dot
                    self.res.append(cur[:-1])
                return
            if len(remain) >= 1:
                dfs(seperated+1, remain[1:], cur + remain[:1] + '.')
            if len(remain) >= 2 and remain[0] != '0':
                dfs(seperated+1, remain[2:], cur + remain[:2] + '.')
            if len(remain) >= 3 and remain[0] != '0' and int(remain[:3]) <= 255:
                dfs(seperated+1, remain[3:], cur + remain[:3] + '.')
        dfs(0, s, '')
        return self.res
                
