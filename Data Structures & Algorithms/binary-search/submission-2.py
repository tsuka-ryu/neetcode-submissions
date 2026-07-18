class Solution:
    def search(self, num, target):
        l, r = 0, len(num) - 1

        while l <= r:
            m = l + (r - l) // 2

            if num[m] > target:
                r = m - 1
            elif num[m] < target:
                l = m + 1
            else:
                return m
        return -1
