class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = counter = 0
        for num in nums:
            counter = counter * num + num
            max_counter = max(max_counter, counter)
        return max_counter