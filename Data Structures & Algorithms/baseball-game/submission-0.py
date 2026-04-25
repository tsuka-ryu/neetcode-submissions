class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for op in operations:
            if op == "+":
                r = ans[-1]
                l = ans[-2]
                ans.append(r + l)
            elif op == "D":
                ans.append(ans[-1] * 2)
            elif op == "C":
                ans.pop(-1)
            else:
                ans.append(int(op))
        return sum(ans)
