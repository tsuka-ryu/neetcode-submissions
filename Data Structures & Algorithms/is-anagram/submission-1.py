class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def countChar(string):
            count = {}

            for i in string:
                if i in count:
                    count[i] +=1
                else:
                    count[i] = 1
            return count

        return countChar(s) == countChar(t)
