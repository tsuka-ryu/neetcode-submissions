class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            maxi = 0
            for j in range(i + 1, len(arr)):
                maxi = max(maxi, arr[j])

            arr[i] = maxi
        arr[-1] = -1
        return arr
