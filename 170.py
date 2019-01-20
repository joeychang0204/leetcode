class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.d[number] = self.d.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.d:
            if  value - num in self.d and num != value-num:
                return True
            elif num == value-num and self.d[num] > 1:
                return True
        return False


class TwoSum2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.l.append(number)
        
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        self.l.sort()
        l, r = 0, len(self.l)-1
        while l < r:
            if self.l[l] + self.l[r] == value:
                return True
            elif self.l[l] + self.l[r] < value:
                l += 1
            else:
                r -= 1
        return False
