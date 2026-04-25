class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        res = 0
        for i in nums:
            if i == 1:
                res += 1
                ans = max(ans, res)
            else:
                res = 0

        return ans
