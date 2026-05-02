class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles, h, k):
            sum = 0
            for i in piles:
                sum += math.ceil(i / k)

            if sum <= h:
                return True
            return False

        left, right = 1, 1000000000
        mini = 1000000000
        while left <= right:
            k = (left + right) // 2
            if canEat(piles, h, k):
                mini = k
                right = k - 1
            else:
                left = k + 1
        return mini
