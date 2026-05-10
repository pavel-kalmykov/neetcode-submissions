class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concat = [None] * (n * 2)
        for i in range(n):
            concat[i] = nums[i]
        for i in range(n):
            concat[n + i] = nums[i]
        return concat