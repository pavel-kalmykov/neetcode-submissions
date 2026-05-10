from io import StringIO
from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        with StringIO() as buffer:
            for str in strs:
                buffer.write(f"{len(str)}#{str}")
            return buffer.getvalue()

    def decode(self, s: str) -> List[str]:
        decoded = []
        skip = 0
        while skip < len(s):
            with StringIO() as buffer:
                while s[skip] != "#":
                    buffer.write(s[skip])
                    skip += 1
                offset = int(buffer.getvalue())
            decoded.append(s[skip + 1 : skip + 1 + offset])
            skip += offset + 1
        return decoded
