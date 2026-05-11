class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
            elif not stack or matches[c] != stack.pop():
                return False
        
        return not stack