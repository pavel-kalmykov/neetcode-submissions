class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = counter = 0
        for num in nums:
            if num == 0:
                max_counter = max(max_counter, counter)
                counter = 0
            else:
                counter += 1
        return max(max_counter, counter)