# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(s, m, e):
            L = pairs[s : m + 1]
            R = pairs[m + 1 : e + 1]

            l = r = 0  # for L & R
            i = s  # for pairs

            while l < len(L) and r < len(R):
                if L[l].key <= R[r].key:
                    pairs[i] = L[l]
                    l += 1
                else:
                    pairs[i] = R[r]
                    r += 1
                i += 1

            while l < len(L):
                pairs[i] = L[l]
                l += 1
                i += 1
            while r < len(R):
                pairs[i] = R[r]
                r += 1
                i += 1
            
        def merge_sort(s, e):
            if e - s + 1 <= 1:
                return
            m = (s + e) // 2
            merge_sort(s, m)
            merge_sort(m + 1, e)

            merge(s, m , e)
        
        merge_sort(0, len(pairs))
        return pairs
