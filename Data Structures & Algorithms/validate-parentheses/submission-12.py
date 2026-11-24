class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif not stack or brackets[c] != stack.pop():
                return False
        return not stack