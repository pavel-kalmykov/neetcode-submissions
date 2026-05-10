class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for c in s:
            if c in ")}]":
                if not stack or par_map[c] != stack.pop():
                    return False
                continue
            stack.append(c)
        return not stack