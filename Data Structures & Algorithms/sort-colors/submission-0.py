class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0, 0, 0]
        for i in nums:
            bucket[i] += 1

        offset = 0
        for i, count in enumerate(bucket):
            for j in range(count):
                nums[offset + j] = i
            offset += count
