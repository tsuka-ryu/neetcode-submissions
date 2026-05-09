class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        res = []
        while 0 < k:
            max_key = max(count, key=count.get)
            res.append(max_key)
            count.pop(max_key)
            k -= 1

        return res
