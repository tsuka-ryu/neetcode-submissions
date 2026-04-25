class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == "{":
                stack.append("{")
            elif c == "[":
                stack.append("[")
            elif c == ")":
                if not stack:
                    return False

                p = stack.pop()
                if p == "(":
                    continue
                else:
                    return False
            elif c == "}":
                if not stack:
                    return False

                p = stack.pop()
                if p == "{":
                    continue
                else:
                    return False
            elif c == "]":
                if not stack:
                    return False

                p = stack.pop()
                if p == "[":
                    continue
                else:
                    return False
        return len(stack) == 0
