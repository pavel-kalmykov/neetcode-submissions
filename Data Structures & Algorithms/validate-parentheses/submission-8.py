class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for c in s:
            print(f"{c=}, {stack=}")
            if c in "([{":
                print(f"adding {c=}")
                stack.append(c)
            elif not stack or matches[c] != stack.pop():
                return False
        
        return not stack