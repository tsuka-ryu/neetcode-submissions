class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        prevRow = [1] * cols

        for r in range(rows - 1):
            curRow = [1] * cols
            for c in range(cols - 2, -1, -1):
                curRow[c] = curRow[c + 1] + prevRow[c]
            prevRow = curRow
        return prevRow[0]
