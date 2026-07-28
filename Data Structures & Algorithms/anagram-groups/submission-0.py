from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                key[index] += 1
            mydict[tuple(key)].append(s)
        return list(mydict.values())