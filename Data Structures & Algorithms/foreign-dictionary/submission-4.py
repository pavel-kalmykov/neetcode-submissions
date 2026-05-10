class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def topological_sort(letter: str) -> bool:
            if letter in visited:
                return visited[letter]
            visited[letter] = True

            for neighbour in adj[letter]:
                if topological_sort(neighbour):
                    return True

            top_sort.append(letter)
            visited[letter] = False
            return False

        adj = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            min_len = min(len(a), len(b))
            if len(a) > len(b) and a[:min_len] == b[:min_len]:
                return ""
            for j in range(min_len):
                if a[j] != b[j]:
                    adj[a[j]].add(b[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        top_sort = []
        for letter in adj:
            if topological_sort(letter):
                return ""

        top_sort.reverse()
        return "".join(top_sort)
