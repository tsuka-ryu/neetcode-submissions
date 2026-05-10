class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes = []
        for s in strs:
            sizes.append(len(s))

        res = ""
        for s in sizes:
            res += str(s)
            res += ","
        res += "#"

        for s in strs:
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        while s[i] != "#":
            i += 1

        nums = s[:i]
        strs = s[i + 1 :]

        sizes = []
        cur = 0
        while len(nums) != cur:
            n = ""
            while nums[cur] != ",":
                n += nums[cur]
                cur += 1
            sizes.append(int(n))
            cur += 1

        res = []
        cur = 0
        for i in sizes:
            res.append(strs[cur : cur + i])
            cur += i
        return res
