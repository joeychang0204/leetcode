class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for letter in word:
            if letter not in cur.child:
                cur.child[letter] = TrieNode()
            cur = cur.child[letter]
        cur.isEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        self.res = False
        def dfs(node, word):
            if self.res:
                return
            if len(word) == 0:
                if node.isEnd:
                    self.res = True
                return
            if word[0] == '.':
                for c in node.child.values():
                    dfs(c, word[1:])
            else:
                if word[0] in node.child:
                    dfs(node.child[word[0]], word[1:])
            return
        dfs(self.root, word)
        return self.res
            
        
class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.isEnd = False
