class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = collections.defaultdict(list)
        for word in dictionary:
            abb = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
            # WA : for repeated words, only add once
            if word not in self.d[abb]:
                self.d[abb].append(word)
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abb = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
        # WA: self.d[abb] is a list, have to give it an index
        return len(self.d[abb]) == 0 or (len(self.d[abb]) == 1 and self.d[abb][0] == word)
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
