# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        steps = [pairs.copy()] if pairs else []
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                aux = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = aux
                j -= 1
            steps.append(pairs.copy())
        return steps