class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for i in s:
            if i not in sMap:
                sMap[i] = 1
            else:
                sMap[i] += 1

        tMap = {}
        for j in t:
            if j not in tMap:
                tMap[j] = 1
            else:
                tMap[j] += 1

        return sMap == tMap
