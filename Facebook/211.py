class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = trie_node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = trie_node()
            node = node.children[letter]
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.res = False
        def search_node(node, start):
            if start == len(word):
                if node.isEnd:
                    self.res = True
                return
            letter = word[start]
            if letter == '.':
                for child in node.children.values():
                    search_node(child, start + 1)
            else:
                if letter not in node.children:
                    return
                search_node(node.children[letter],start + 1)
        search_node(self.root,  0)
        return self.res

class trie_node:
    def __init__(self):
        self.children = {}
        self.isEnd = False


wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print(wd.search("pad"))
print(wd.search("bad"))
print(wd.search(".ad"))
print(wd.search("b.."))
