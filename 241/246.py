class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        return all(num[i] + num[len(num)-1-i] in ['69', '96', '88', '00', '11']
                  for i in range(len(num)))
