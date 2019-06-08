class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        s = ''
        for string in strs:
            s += str(len(string)) + '/' + string
        return s

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            # find the slash's position
            j = s.find('/', i+1)
            length = int(s[i:j])
            strs.append(s[j+1:j+length+1])
            i = j+length+1
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
