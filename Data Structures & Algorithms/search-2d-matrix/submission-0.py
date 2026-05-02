class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        xl, xr = 0, len(matrix) - 1
        x = -1

        while xl <= xr:
            mid = (xl + xr) // 2

            if target < matrix[mid][0]:
                xr = mid - 1
            elif target > matrix[mid][-1]:
                xl = mid + 1
            else:
                x = mid
                break

        if x == -1:
            return False

        yl, yr = 0, len(matrix[x]) - 1
        y = -1
        while yl <= yr:
            mid = (yl + yr) // 2

            if target > matrix[x][mid]:
                yl = mid + 1
            elif target < matrix[x][mid]:
                yr = mid - 1
            else:
                y = mid
                break

        if y == -1:
            return False
        return True
