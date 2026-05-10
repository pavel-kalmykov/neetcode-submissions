class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif not stack or par_map[c] != stack.pop():
                return False
        return not stack