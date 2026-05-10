# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.__quick_sort_recursive(pairs, 0, len(pairs) - 1)
        return pairs

    def __quick_sort_recursive(
        self,
        pairs: List[Pair],
        start: int,
        end: int,
    ) -> None:
        if end - start <= 0:
            return

        left = start
        pivot = pairs[end]
        for i in range(start, end):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1
        pairs[end], pairs[left] = pairs[left], pivot

        self.__quick_sort_recursive(pairs, start, left - 1)
        self.__quick_sort_recursive(pairs, left + 1, end)

