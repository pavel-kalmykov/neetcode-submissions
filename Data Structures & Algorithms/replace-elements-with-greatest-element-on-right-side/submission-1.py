class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        curr_max = arr[-1]
        replaced = [-1] * n
        for i in range(n - 2, -1, -1):
            replaced[i] = curr_max
            curr_max = max(curr_max, arr[i])
        return replaced