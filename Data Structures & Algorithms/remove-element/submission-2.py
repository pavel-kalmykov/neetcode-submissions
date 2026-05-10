class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            nums[k] = nums[i]
            if nums[i] != val:
                k += 1
        return k