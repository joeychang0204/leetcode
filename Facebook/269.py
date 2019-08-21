import collections
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # case: ['z', 'z']
        edges = collections.defaultdict(list)
        inDegree = collections.defaultdict(int)
        zeroDegree = []
        # set('yuan') -> {'y', 'u', 'a', 'n'}
        all_letters = set(''.join(words))
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            len1, len2 = len(word1), len(word2)
            # find the first different letter. Don't forget to break!
            for j in range(min(len1, len2)):
                if word1[j] != word2[j]:
                    inDegree[word2[j]] += 1
                    edges[word1[j]].append(word2[j])
                    break
        res = ''
        # find the zero degrees
        for letter in all_letters:
            if inDegree[letter] == 0:
                zeroDegree.append(letter)
        while zeroDegree:
            cur = zeroDegree.pop()
            res += cur
            for neighbor in edges[cur]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    zeroDegree.append(neighbor)
        return '' if len(res) != len(all_letters) else res

print(Solution().alienOrder(["za","zb","ca","cb"]))
print(set('yuan'))
