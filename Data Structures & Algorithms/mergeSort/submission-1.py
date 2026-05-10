class Solution:

    def __merge(self, pairs: List[Pair], start: int, mid: int, end: int):
        pairs_copy = pairs[start:end + 1]
        i = pos = start
        j = mid + 1
        while i <= mid and j <= end:
            if pairs_copy[i - start].key <= pairs_copy[j - start].key:
                pairs[pos] = pairs_copy[i - start]
                i += 1
            else:
                pairs[pos] = pairs_copy[j - start]
                j += 1
            pos += 1
        while i <= mid:
            pairs[pos] = pairs_copy[i - start]
            i += 1
            pos += 1
        while j <= end:
            pairs[pos] = pairs_copy[j - start]
            j += 1
            pos += 1

    def __merge_sort(self, pairs: List[Pair], start: int, end: int):
        if end - start <= 0:
            return
        mid = (end - start) // 2 + start
        self.__merge_sort(pairs, start, mid)
        self.__merge_sort(pairs, mid + 1, end)
        self.__merge(pairs, start, mid, end)

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.__merge_sort(pairs, 0, len(pairs) - 1)
        return pairs
