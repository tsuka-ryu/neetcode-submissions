class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}

        for i in nums:
            if i not in countMap:
                countMap[i] = 1
            else:
                return True
        
        return False