class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x * x + y * y, [x, y]) for x, y in points]
        heapq.heapify(heap)

        ans = []
        while k > 0:
            dist, p = heapq.heappop(heap)
            ans.append(p)
            k -= 1

        return ans