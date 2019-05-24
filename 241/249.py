class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # WA : az, ba -> have to %26
        grouped = {}
        for s in strings:
            key = str(len(s))
            for i in range(len(s)):
                if i == 0:
                    continue
                key += str((ord(s[i])-ord(s[i-1])) % 26)
            grouped[key] = grouped.get(key, []) + [s]
        # RE: values not returning list in Python3, have to wrap
        return list(grouped.values())
